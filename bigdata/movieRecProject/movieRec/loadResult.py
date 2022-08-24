import sqlite3
from os.path import join


# 파일을 읽어 들여 SQLite3 데이터베이스에 사용


def load_movies(cur):
    # m1-1m-movies.dat 데이터 파일에서 모든 영화의 id, title, text를 읽어서 튜플(id, title, text)를 만들어서 movieRec_movie 테이블에 삽입
    path = 'matrixFactorization/data/movielens-1m/ml-1m_movies.dat'
    # 혹시 다른 것이 저장되어 있다면 없애고 새로 시작
    cur.execute('DELETE FROM movieRec_movie')
    # 파일을 열어 하나씩 읽으면서
    with open(path, encoding='latin-1') as f:
        for line in f:
            #line = line.replace('\'', '\\\'')
            token = line.strip().split('::')
            id = token[0]
            title, year = token[1].rsplit(' ', 1)
            year = year[1:-1]
            text = token[2]
            #print(id, title, year)
            #print('INSERT INTO movieRec_movie(id, title, text) VALUES(\'%s\',\'%s\',\'%s\')'%(tuple(token)) )
            try: cur.execute('INSERT INTO movieRec_movie(id, title, text, year) VALUES(?,?,?,?)', (id, title, text, year))
            except: pass


def load_viewed(cur, model_home):
    path = join(model_home, 'train_ratings.txt')
    # 항상 가장 먼저 SQLite3 데이터베이스에 있는 movieRec_viewed 테이블의 내용 삭제
    cur.execute('DELETE FROM movieRec_viewed')
    with open(path) as f:
        for line in f:
            token = line.strip().split('::')
            cur.execute('SELECT COUNT(*) FROM movieRec_user WHERE id=?', (token[0],))
            n_rows = cur.fetchall()[0][0]
            if n_rows == 0:
                cur.execute('INSERT INTO movieRec_user(id, name) VALUES(?,?)', (token[0], 'User%05d'%(int(token[0]))))
            cur.execute('INSERT INTO movieRec_viewed(user_id, movie_id, rating) VALUES(?,?,?)', (token[0], token[1],token[2]) )

# 실습
def load_recomm(cur, model_home):
    # 예상 평점은 recommend_ratings.txt 파일에 들어 있음
    path = join(model_home, 'recommend_ratings.txt')
    # 맨 먼저 SQLite3 데이터베이스에 있는 movieRec_recomm 테이블의 내용 삭제
    cur.execute('DELETE FROM movieRec_recomm')
    with open(path) as f:
        for line in f:
            token = line.strip().split('::')
            cur.execute('INSERT INTO movieRec_recomm(user_id, movie_id, score) VALUES(?,?,?)', (token[0], token[1], token[2]))
            

def load_result(model_home):
    conn= sqlite3.connect('./db.sqlite3')
    cur = conn.cursor()

    # 예상 영화 평점 데이터를 load_movies, load_viewed, load_recomm 함수들을 각각 호출하여 SQlite3 데이터베이스에 있는 테이블들에 저장
    print("LOAD MOVIEDATA")
    load_movies(cur)
    print("LOAD VIEWED DATA")
    load_viewed(cur, model_home)
    print("LOAD RECOMM DATA")
    load_recomm(cur, model_home)
    print("load_result IS FINISHED")

    conn.commit()
    conn.close()


if __name__ == '__main__':
    conn= sqlite3.connect('../db.sqlite3')
    cur = conn.cursor()
    #load_movies()
    #load_viewed(cur)
    #load_recomm()
    conn.commit()
    conn.close()



import argparse
import sys
import pickle
import numpy as np
from models import knn, matrix_factorization, plsi

'''
입력 파라미터

-i: 데이터 파일이 있는 디렉토리 이름
-o: 결과 저장 디렉토리
-a: 번호 (학습 알고리즘 선택 번호)
    - 번호가 0이면 run_kNN 함수를 호출하고
    - 번호가 1이면 run_MF 함수를 호출하고
    - 번호가 2이면 run_MF_PLSI 함수를 호출
-k: kNN 알고리즘에서 추천에 사용하는 이웃의 개수 (default값은 5)

* 필요한 입력 파라미터가 제공되지 않으면 에러 메시지를 출력하고 종료
'''

# load() 함수를 이용하여 pickle 모듈로 생성된 파일 R_train.pkl과 item_ids.pkl을 input_path의 디렉토리에서 읽음
def load(path):
    return pickle.load(open(path, "rb"))


def recommend(R_train, R_predicted, item_ids, output_path):
    # write train ratings
    # write recommend ratings
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # command line parameter check
    # add_argument 이용해 파라미터 정의
    parser.add_argument("-a", "--algorithm", type=int, help="algorithm 0 (knn), 1 (mf), 2 (plsi+mf)")
    parser.add_argument("-i", "--input_path", type=str, help="Path input data pickle")
    parser.add_argument("-o", "--output_path", type=str, help="Output path")
    parser.add_argument("-d", "--dim", type=int, help="Size of latent dimension (default: 50)", default=50)
    parser.add_argument("-u", "--lambda_u", type=float, help="User Regularization", default=10)
    parser.add_argument("-v", "--lambda_v", type=float, help="Item Regularization", default=100)
    parser.add_argument("-m", "--max_iter", type=int, help="Max Iteration (default: 200)", default=30)
    parser.add_argument("-k", "--k", type=int, help="k for knn", default=5)
    args = parser.parse_args()

    input_path = args.input_path
    if input_path is None:  # 입력되지 않은 경우
        sys.exit("input_path is required")
    output_path = args.output_path
    if output_path is None:
        sys.exit("output_path is required")

    R_train = load(input_path + '/R_train.pkl')
    R_valid = load(input_path + '/R_valid.pkl')
    item_ids = load(input_path + '/item_ids.pkl')

    alg = args.algorithm    # 입력한 번호를 받아 옴
    if alg == 0:
        # KNN
        k = args.k
        R_predicted = knn.predict(R_train, k)
        # recommend 함수 호출
        recommend(R_train, R_predicted, item_ids, '.')

    elif alg == 1 or alg == 2:
        d = args.dim
        lambda_u = args.lambda_u
        lambda_v = args.lambda_v
        max_iter = args.max_iter

        theta = None    # theta: PLSI가 만들어낸 결과 가져옴
        if alg == 2:
            # PLSI
            print("\n\t start training PLSI")
            theta = plsi.train(input_path, d, False)
            pass
        # Matrix Factorization
        print()
        print("\n\t start training MF")
        R_predicted = matrix_factorization.train(res_dir=output_path, R_train=R_train, R_valid=R_valid,
                                   max_iter=max_iter, lambda_u=lambda_u, lambda_v=lambda_v, dimension=d, theta=theta)
        recommend(R_train, R_predicted, item_ids, '.') 
    else:
        print("select algorithm from 0 to 2")


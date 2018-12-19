from flask import Flask, request, jsonify


ERROR_MESSAGE = '네트워크 접속에 문제가 발생하였습니다. 잠시 후 다시 시도해주세요.'


app = Flask(__name__)


# 피자 주문 스킬
@app.route('/order', methods=['POST'])
def order():

    # 메시지 받기
    req = request.get_json()

    pizza_type = req["action"]["detailParams"]["피자종류"]["value"]
    address = req["action"]["detailParams"]["sys_text"]["value"]

    if len(pizza_type) <= 0 or len(address) <= 0:
        answer = ERROR_MESSAGE
    else:
        answer = pizza_type + "를 '" + address + "'(으)로 배달하겠습니다.주문 감사합니다~"

    # 메시지 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    return jsonify(res)


# 메인 함수
if __name__ == '__main__':

    app.run(host='0.0.0.0', threaded=True)


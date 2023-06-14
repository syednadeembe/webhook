from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/validate', methods=['POST'])
def validate():
    admission_review = request.get_json()
    pod = admission_review['request']['object']

    # Check if the pod is missing the securityContext
    if 'securityContext' not in pod.get('spec', {}):
        admission_response = {
            'apiVersion': 'admission.k8s.io/v1',
            'kind': 'AdmissionReview',
            'response': {
                'uid': admission_review['request']['uid'],
                'allowed': False,
                'status': {
                    'code': 403,
                    'message': 'Pod is missing securityContext',
                },
            },
        }
        return jsonify(admission_response)

    # Pod is valid, allow the request
    admission_response = {
        'apiVersion': 'admission.k8s.io/v1',
        'kind': 'AdmissionReview',
        'response': {
            'uid': admission_review['request']['uid'],
            'allowed': True,
        },
    }
    return jsonify(admission_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


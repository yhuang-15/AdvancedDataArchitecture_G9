def execute_workflow_get_result(request):
    import requests
    from flask import abort, jsonify
    import json
    import time
    import logging
    
    logging.basicConfig(level=logging.INFO)

    inputs = request.get_json(silent=True)
    host = "https://workflowexecutions.googleapis.com/"
    url_post = f"/v1/projects/jads-de-2021/locations/us-central1/workflows/{inputs['workflow']}/executions"
    
    # arguments needed for executing the workflow
    # no arguments needed: '' - empty string
    # could also get from request body: inputs['payload']
    payload_get = '{\"argument\": \"{\\\"' + 'a_id' + '\\\":\\' + str(inputs['a_id']) + '\\, \\\"' + 'applyID' + '\\\":\\\"' + inputs['applyID'] + '\\\", \\\"' + 'aptID' + '\\\":\\\"' + inputs['aptID'] + '\\\"}\"}' 

    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {inputs['googleKey']}"
    }

    try:
        # execute the workflow
        url = host + url_post
        response = requests.request("POST", url, data=payload_get, headers=headers)
        response = json.loads(response.text)
        logging.info(f""" Post result: {response}
            """)

        # get the results after executing the workflow
        execute_path_with_eid = response['name'].split('/')
        e_id = execute_path_with_eid[-1]
        del response
        time.sleep(2)

        url_get = url + '/' + e_id
        response_get = requests.request("GET", url_get, data='', headers=headers).text
        response_get = json.loads(response_get)
        logging.info(f""" Get result: {response_get}
            """)

        return jsonify(response_get), 200

        #result = response_get['result']
        #return jsonify(result), 200


        #output = json.loads(result)
        #return jsonify(output['body']), 200

    except:
        return abort(405)
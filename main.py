from api.campaign_api import CreateCampaignAPI, DeleteCampaignAPI, UpdateCampaignAPI, GetCampaignAPI, GetEditableCampaignAPI
from api.flow_api import CreateFlowAPI, DeleteFlowAPI, UpdateFlowAPI, GetFlowAPI
from api.search_api import SearchAPI
import logging
from flask_restful import Api
from flask import Flask
from flask_cors import CORS


__LOG_FORMAT = '[%(asctime)s][%(levelname)s] %(message)s'
logging.basicConfig(format=__LOG_FORMAT, level=logging.DEBUG)

app = Flask(__name__,
            static_folder="./vue_frontend/dist/static",
            template_folder="./vue_frontend/dist")
app.url_map.strict_slashes = False
api = Api(app)
CORS(app,
     allow_headers=["Content-Type",
                    "Authorization",
                    "Access-Control-Allow-Credentials"],
     supports_credentials=True)

api.add_resource(SearchAPI, '/api/search')

api.add_resource(CreateCampaignAPI, '/api/campaigns/create')
api.add_resource(DeleteCampaignAPI, '/api/campaigns/delete')
api.add_resource(UpdateCampaignAPI, '/api/campaigns/update')
api.add_resource(GetCampaignAPI, '/api/campaigns/get/<string:prepid>')
api.add_resource(GetEditableCampaignAPI, '/api/campaigns/get_editable', '/api/campaigns/get_editable/<string:prepid>')

api.add_resource(CreateFlowAPI, '/api/flows/create')
api.add_resource(DeleteFlowAPI, '/api/flows/delete')
api.add_resource(UpdateFlowAPI, '/api/flows/update')
api.add_resource(GetFlowAPI, '/api/flows/get/<string:prepid>')


app.run(host='0.0.0.0',
        port=8004,
        threaded=True,
        debug=True)

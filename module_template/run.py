#!/usr/bin/env python
from dotenv import load_dotenv
from typing import Dict
from naptha_sdk.schemas import AgentRunInput
from naptha_sdk.user import sign_consumer_id
from naptha_sdk.utils import get_logger
from web3.types import TxParams

from module_template.schemas import InputSchema

load_dotenv()

logger = get_logger(__name__)

# You can create your module as a class or function
class OmenBuyTransactionModule:
    """ Returns TxParams for buying outcome tokens from a given Omen market on Gnosis chain. """
    def __init__(self, module_run):
        self.module_run = module_run

    def func(self, input_data):
        logger.info(f"Running module function")
        tx_params: TxParams = {}
        return tx_params

# Default entrypoint when the module is executed
def run(module_run: Dict):
    module_run = AgentRunInput(**module_run)
    module_run.inputs = InputSchema(**module_run.inputs.model_dump())
    basic_module = OmenBuyTransactionModule(module_run)
    method = getattr(basic_module, module_run.inputs.func_name, None)
    return method(module_run.inputs.func_input_data)

if __name__ == "__main__":
    import asyncio
    from naptha_sdk.client.naptha import Naptha
    from naptha_sdk.configs import setup_module_deployment
    import os

    naptha = Naptha()

    deployment = asyncio.run(setup_module_deployment("agent", "module_template/configs/deployment.json", node_url = os.getenv("NODE_URL")))

    input_params = InputSchema(market_id= "0x123",
                               from_address="0x456",
                               collateral_wei_amount=1000000000000000000,
                               func_name= "func",
                func_input_data='gm...',
    )


    module_run = {
        "inputs": input_params,
        "deployment": deployment,
        "consumer_id": naptha.user.id,
        "signature": sign_consumer_id(naptha.user.id, os.getenv("PRIVATE_KEY"))
    }

    response = run(module_run)

    print("Response: ", response)
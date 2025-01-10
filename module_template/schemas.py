from typing import Optional, Union, Dict, Any, List

from hexbytes import HexBytes
from pydantic import BaseModel
from web3.types import Wei


class InputSchema(BaseModel):
    # ToDo - Use HexBytes and Wei once PMAT available.
    market_id: str
    from_address: str
    collateral_wei_amount: int
    # ToDo - Why do I define func_name and func_input_data here?
    func_name: str
    func_input_data: Optional[Union[Dict[str, Any], List[Dict[str, Any]], str]] = None

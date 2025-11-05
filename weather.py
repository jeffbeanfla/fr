
import time
import datetime
from datetime import date
from datetime import datetime
import python_weather

import asyncio
import os

async def main():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Fort Lauderdale')
        #now=time.localtime()
        now=datetime.now()
        ftoday= now.strftime("%H:%M:%S")
        print ("Today:",date.today(),"At:",ftoday ,"Temp:", weather.temperature,  "Outlook: ", weather.kind)
        
asyncio.run(main())


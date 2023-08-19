#!/usr/bin/env python3
import uvicorn
from expenseman.config import Config

uvicorn.run("expenseman:main", port=Config.PORT, log_level="info", factory=True)
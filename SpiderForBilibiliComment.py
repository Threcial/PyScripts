import pandas
import requests

target_url = 'https://www.bilibili.com/video/BV1E3yUBLE5c'

header = {
    'Cookie' : 'enable_web_push=DISABLE; buvid_fp_plain=undefined; home_feed_column=5; DedeUserID=1000541639; DedeUserID__ckMd5=5116ae25439115e7; enable_feed_channel=ENABLE; CURRENT_QUALITY=80; buvid3=18C5078E-5602-34F6-08B9-E6C4D0DE441686886infoc; b_nut=1744175386; _uuid=EB9105C210-F1BF-E105E-C106A-E337EEFFCD9487721infoc; hit-dyn-v2=1; fingerprint=1f2ef51b8f975f70b1f0b61256965ac7; rpdid=|(J|)Rl|kllu0J\'u~R~ulu|u|; buvid_fp=1f2ef51b8f975f70b1f0b61256965ac7; browser_resolution=1552-831; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; theme_style=dark; LIVE_BUVID=AUTO1117535311888444; buvid4=4F3DFB22-1C94-F123-ADC0-9D38C6BFBBBE25355-024040811-fN9XNMApJhFy91kX3+X15A%3D%3D; PVID=1; CURRENT_FNVAL=4048; b_lsid=2C8DCC7C_19A38E19245; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NjIxNTAwOTgsImlhdCI6MTc2MTg5MDgzOCwicGx0IjotMX0.EHg89qSLi0Z9U0c0SgRXUc2fVDm2MVPvXH3-6LFsZDQ; bili_ticket_expires=1762150038; SESSDATA=27d4aeb7%2C1777442899%2C5f997%2Aa1CjALRl6RAKGHpA_9zhY6Cjwy51aJcZSH3ye46otZMjSd31XW09T3xUPmXp6KZTRRpF4SVm9Cemk0Y3BibGstLUh2a0NBSjJBZW5KRzY1aFZiLVdsQnJCQlJwUUJ3ZUVCQVlRVzdlaHoyUUV2b3liLXVjTExfdy1yWW1pN2pRYlNYeGVQOEEtLWRRIIEC; bili_jct=a2df080961c16fefc3615a226259f45e; sid=ptiowqdn; bp_t_offset_1000541639=1129801893220974592',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}

response = requests.get(target_url, header)
print(response)
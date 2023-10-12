from bilibili_api.search import search_by_type, SearchObjectType, OrderVideo
from bilibili_api.video import Video, VideoAppealReasonType
from bilibili_api import Credential
import asyncio, json, random, time, os

banned_words = ["反和谐", "fhx", "真名", "名字"]
report_reason = ["宣传游戏外挂", "发表不实消息", "发布引战言论", "宣扬游戏漏洞", "恶意使用和传播游戏漏洞"]

credential = Credential(
    ac_time_value=None
    )

async def find_sensitive_videos() -> list:
    """
    搜索敏感视频
    """
    vlist = []

    all_list = await search_by_type(
        "碧蓝航线",
        SearchObjectType.VIDEO,
        OrderVideo.PUBDATE,
        )  # 按时间搜索视频
    
    for video in all_list["result"]:
        for word in banned_words:
            if word in video["title"] or word in video["description"]:  # 检查视频标题与简介是否有违禁词
                vlist.append(video)
                break
    
    if len(vlist) == 0:
        print("本次未搜索到敏感视频")
    else:
        print(f"本次共搜索到{len(vlist)}个敏感视频，分别为：")
        for video in vlist:
            print(f"av{video['bvid']} {video['title']}")

    return [video["bvid"] for video in vlist]

async def report_videos(video_list: list):
    """
    举报敏感视频
    """
    for video in video_list:
        v = Video(bvid=video, credential=credential)
        ret = await v.appeal(VideoAppealReasonType.LEAD_WAR, random.choice(report_reason))  # 举报

        time.sleep(3)
    
async def main():
    while True:
        vlist = await find_sensitive_videos()
        await report_videos(vlist)

        time.sleep(60 * 10)  # 间隔十分钟

if __name__ == '__main__':
    print("获取方式：https://nemo2011.github.io/bilibili-api/#/get-credential")
    print("请输入B站Cookie认证字段（特别注意：请勿泄露给他人，否则后果自负）:")
    if os.path.exists("credential.json"):
        with open("credential.json", "r", encoding="utf-8") as f:
            cot = json.load(f)
        credential.sessdata = cot["sessdata"]
        credential.bili_jct = cot["bili_jct"]
        credential.buvid3 = cot["buvid3"]
        credential.dedeuserid = cot["dedeuserid"]
    else:
        credential.sessdata = input("SESSDATA:")
        credential.bili_jct = input("bili_jct:")
        credential.buvid3 = input("buvid3:")
        credential.dedeuserid = input("DedeUserID:")

        with open("credential.json", "w", encoding="utf-8") as f:
            json.dump(credential.__dict__, f, ensure_ascii=False, indent=4)

    asyncio.get_event_loop().run_until_complete(main())
key = "e87c4053cc814a338a2090130c2424c7"
endpoint = "https://cog-openai-test-dev.openai.azure.com/"


#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://cog-openai-test-dev.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  engine="milize-dev-gpt35-turbo-0301",
  prompt="記事から「容疑者」「国籍」「年齢」「住所」「所属団体」を抽出、\n# 記事開始\n\n\n衣服のボタンは覚醒剤、輸入疑いで山口組系組幹部の男逮捕\n衣服のボタンを装って覚醒剤を輸入したとして、大阪府警生野署は６日、覚醒剤取締法違反（営利目的輸入）の疑いで、特定抗争指定暴力団山口組系組幹部で韓国籍、金利和（きんりわ）被告（５２）＝大阪市中央区日本橋、同罪などで起訴＝を逮捕、送検したと発表した。逮捕は昨年１２月９日。「覚醒剤が送られてきたことは分からなかった」と容疑を否認している。\n\n逮捕、送検容疑は何者かと共謀し、昨年２月、営利目的で覚醒剤１５７グラム（末端価格約９２８万円相当）を国際郵便でイランから輸入したとしている。\n\n覚醒剤はボタンの形に加工されて衣服に縫い付けられていた。関西国際空港で郵便物を検査していた大阪税関職員がボタンの見た目を不審に思って調べ、覚醒剤であることが判明。段ボール２箱に上着８着が入っており、縫い付けられた計８８個のボタンが全て覚醒剤だった。覚醒剤をボタンに加工する手口は極めて珍しいという。\n\n郵便物は大阪市生野区に住む金被告の知人男性宛てで、同署は昨年１１月、同容疑で男性を逮捕。嫌疑不十分で不起訴となったが、男性の供述などから金被告の関与が浮上した。\n# 記事終了\n\n# 容疑者\n金利和（きんりわ）被告\n\n# 国籍\n韓国籍\n\n# 年齢\n52\n\n# 住所\n大阪市中央区日本橋\n\n# 所属団体\n特定抗争指定暴力団山口組系組幹部\n<|im_end|>",
  temperature=0.3,
  max_tokens=350,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)
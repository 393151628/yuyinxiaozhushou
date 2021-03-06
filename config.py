APPID1 = "5b7a65f0"
video2text_api_key = "08bc221f2045757db27fb5384d7f47d1"
words_api_key = 'dd2e73409172636d565f5b8b710dcf22'
action_list = ['cws', 'pos', 'ner', 'dp', 'sdp', 'srl']
REDIRECT = ['通讯录', '邮箱', '短信']
PHONENUMBER = ['电话', '手机', '号', '座机号', '号码']
# EXCUSEORDER = ['邮件', '电话', '短信', '打电话', '发短信']
EXCUSEORDER = ['电话', '打电话']
DP_DICT = {
    'ADV': ('状中结构', 'adverbial', '非常美丽 (非常 \\<-- 美丽)'),
    'ATT': ('定中关系', 'attribute', '红苹果 (红 \\<-- 苹果)'),
    'CMP': ('动补结构', 'complement', '做完了作业 (做 --> 完)'),
    'COO': ('并列关系', 'coordinate', '大山和大海 (大山 --> 大海)'),
    'DBL': ('兼语', 'double', '他请我吃饭 (请 --> 我)'),
    'FOB': ('前置宾语', '前置宾语，fronting-object', '他什么书都读 (书 \\<-- 读)'),
    'HED': ('核心关系', 'head', '指整个句子的核心'),
    'IOB': ('间宾关系', '间接宾语，indirect-object', '我送她一束花 (送 --> 她)'),
    'IS': ('独立结构', 'independent structure', '两个单句在结构上彼此独立'),
    'LAD': ('左附加关系', 'left adjunct', '大山和大海 (和 \\<-- 大海)'),
    'POB': ('介宾关系', 'preposition-object', '在贸易区内 (在 --> 内)'),
    'RAD': ('右附加关系', 'right adjunct', '孩子们 (孩子 --> 们)'),
    'SBV': ('主谓关系', 'subject-verb', '我送她一束花 (我 \\<-- 送)'),
    'VOB': ('动宾关系', '直接宾语，verb-object', '我送她一束花 (送 --> 花)'),
    'WP': ('标点', 'punctuation', '。')
}
SDP_DICT = {
    "Accd": ['依据角色', '本庭依法宣判 (依法 \\<-- 宣判)'],
    'Aft': ['感事关系', '我思念家乡 (思念 --> 我)'],
    'Agt': ['施事关系', '我送她一束花 (我 \\<-- 送)'],
    'Belg': ['属事角色', '老赵有俩女儿 (老赵 \\<-- 有)'],
    'Clas': ['类事角色', '他是中学生 (是 --> 中学生)'],
    'Comp': ['比较角色', '他成绩比我好 (他 --> 我)'],
    'Cons': ['结局角色', '他跑了满头大汗 (跑 --> 满头大汗)'],
    'Cont': ['客事关系', '他听到鞭炮声 (听 --> 鞭炮声)'],
    'Datv': ['涉事关系', '他告诉我个秘密 ( 告诉 --> 我 )'],
    'Feat': ['描写角色', '他长得胖 (长 --> 胖)'],
    'Dir': ['趋向角色', '部队奔向南方 (奔 --> 南)'],
    'Exp': ['当事关系', '我跑得快 (跑 --> 我)'],
    'Freq': ['频率角色', '他每天看书 (每天 \\<-- 看)'],
    'Host': ['宿主角色', '住房面积 (住房 \\<-- 面积)'],
    'Int': ['意图角色', '为了金牌他拼命努力 (金牌 \\<-- 努力)'],
    'Loc': ['空间角色', '这房子朝南 (朝 --> 南)'],
    'Malt': ['材料角色', '她用小米熬粥 (小米 \\<-- 熬粥)'],
    'Mann': ['方式角色', '球慢慢滚进空门 (慢慢 \\<-- 滚)'],
    'Nmod': ['名字修饰角色', '果戈里大街 (果戈里 \\<-- 大街)'],
    'Orig': ['源事关系', '我军缴获敌人四辆坦克 (缴获 --> 坦克)'],
    'Pat': ['受事关系', '他打了小明 (打 --> 小明)'],
    'Poss': ['领事关系', '他有一本好读 (他 \\<-- 有)'],
    'Proc': ['历程角色', '火车正在过长江大桥 (过 --> 大桥)'],
    'Prod': ['成事关系', '他写了本小说 (写 --> 小说)'],
    'Qp': ['数量数组', '三本书 (三 --> 本)'],
    'Quan': ['数量角色', '一年有365天 (有 --> 天)'],
    'Reas': ['缘故角色', '他在愁女儿婚事 (愁 --> 婚事)'],
    'Root': ['根节点', '全句核心节点'],
    'Sco': ['范围角色', '产品应该比质量 (比 --> 质量)'],
    'Seq': ['顺序角色', '他跑第一 (跑 --> 第一)'],
    'Tag': ['关系类型', 'Example'],
    'Time': ['时间角色', '唐朝有个李白 (唐朝 \\<-- 有)'],
    'Tmod': ['时间修饰角色', '星期一上午 (星期一 \\<-- 上午)'],
    'Tool': ['工具角色', '她用砂锅熬粥 (砂锅 \\<-- 熬粥)'],
    'd + main role': ['嵌套角色', '爷爷看见孙子在跑 (看见 --> 跑)'],
    'eAban': ['割舍关系', '与其，也不'],
    'eAdvt': ['转折关系', '却，然而'],
    'eCau': ['原因关系', '因为，既然'],
    'eConc': ['让步关系', '纵使，哪怕'],
    'eCond': ['条件关系', '只要，除非'],
    'eCoo': ['并列关系', '我喜欢唱歌和跳舞 (唱歌 --> 跳舞)'],
    'eEqu': ['等同关系', '他们三个人一起走 (他们 --> 三个人)'],
    'eInf': ['推论关系', '才，则'],
    'eMetd': ['手段关系', ''],
    'ePrec': ['先行关系', '首先，先'],
    'ePref': ['选取关系', '不如，宁愿'],
    'eProg': ['递进关系', '况且，并且'],
    'ePurp': ['目的关系', '为了，以便'],
    'eRect': ['分叙关系', '例如，比方说'],
    'eResu': ['结果关系', '因此，以致'],
    'eSelt': ['选择关系', '您是喝茶还是喝咖啡 (茶 --> 咖啡)'],
    'eSucc': ['顺承关系', '随后，然后'],
    'eSum': ['总括关系', '总而言之'],
    'eSupp': ['假设关系', '如果，要是'],
    'mAux': ['的字标记', '的，地，得'],
    'mConj': ['连词标记', '和，或'],
    'mDegr': ['程度标记', '很，稍微'],
    'mDir': ['趋向标记', '上去，下来'],
    'mFreq': ['频率标记', '再，常常'],
    'mMaj': ['多数标记', '们，等'],
    'mMod': ['情态标记', '幸亏，会，能'],
    'mNeg': ['否定标记', '不，没，未'],
    'mPars': ['插入语标记', '总的来说，众所周知'],
    'mPept': ['重复标记', '走啊走 (走 --> 走)'],
    'mPrep': ['介词标记', '把，被'],
    'mPunc': ['标点标记', '，。！'],
    'mRang': ['范围标记', '都，到处'],
    'mSepa': ['离合标记', '吃了个饭 (吃 --> 饭) 洗了个澡 (洗 --> 澡)'],
    'mTime': ['时间标记', '才，曾经'],
    'mTone': ['语气标记', '吗，呢'],
    'mVain': ['实词虚化标记', ''],
    'r + main role': ['反角色', '打篮球的小姑娘 (打篮球 \\<-- 姑娘)']
}



## anwser
URL = "http://openapi.xfyun.cn/v2/aiui"
APPID2 = "5b74da7b"
API_KEY = "c7667bacf4104c71b9b73ad01cafe7a6"
AUE = "raw"
AUTH_ID = "854f28e91e577247dce75254cbaf22d0"
DATA_TYPE = "audio"
SAMPLE_RATE = "16000"
SCENE = "main"
RESULT_LEVEL = "complete"
LAT = "39.938838"
LNG = "116.368624"
#个性化参数，需转义
PERS_PARAM = "{\\\"auth_id\\\":\\\"854f28e91e577247dce75254cbaf22d0\\\"}"
FILE_PATH = "tongxunlu.wav"
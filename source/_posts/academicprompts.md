---
cover: https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021441202.webp
collection:
  profile: topic
  id: prompts
title: 转译-15个适用于学术写作的 ChatGPT Prompts
date: 2024-04-02 09:35:51
tags: [ChatGPT, Prompt]
categories: [AI] 
---

{% quot el:h3 引言 icon:hashtag %}

{% box color:cyan %}
[15 ChatGPT Prompts for Academic Writing](https://www.godofprompt.ai/blog/chatgpt-prompts-for-academic-writing) 这篇文章详细阐述了如何利用 ChatGPT 来增强学术写作的各个方面,帮助学术作者通过生成创意点子、结构化论证、克服写作障碍以及格式化引用来提升学术写作质量。我认为是一篇非常不错的 Prompts ,这 15 条 Prompts 都可以单独提取使用. 是一个很好的学习范例.
{% endbox %}

{% poetry 本文用到的工具们 footer:我认为一个好的&nbsp;Prompts&nbsp;可以一定程度弥补国产大模型的不足 %}
- 月之暗面 moonshot 国产大模型 {% button Kimi https://kimi.moonshot.cn/ size:xs %}.

- 通过 {% button kimi-free-api https://github.com/LLM-Red-Team/kimi-free-api/ size:xs %} 转为 API.
- 在 [Open WebUI](https://github.com/open-webui/open-webui) 使用 {% button 宝玉翻译 https://x.com/geekbb/status/1737634536257995177?s=20 size:xs %} Prompts .
- {% mark 全文翻译采用'意译',仅修改几处,感谢&nbsp;AI&nbsp;工具辛勤付出. color:orange %}
- 所有对话保存在"[chat-学术写作的利器.txt](https://github.com/igeekbb/OSS/blob/main/appendix/chat-%E5%AD%A6%E6%9C%AF%E5%86%99%E4%BD%9C%E7%9A%84%E5%88%A9%E5%99%A8.txt)",有兴趣可以自行查看.
{% endpoetry %}

{% quot el:h3 正文 icon:hashtag %}

```
学术论文写作可能很困难。为了获得更好的结果，你必须研究新的想法并将它们转化为正式的写作。
更不用说在事实核查、准确引用资料以及维持文章客观性方面所面临的压力了。
不过，好消息是：ChatGPT 能成为你学术写作的得力助手。
本文将介绍 15 个 ChatGPT 提示，助你一臂之力。
借助这些提示，ChatGPT 不仅能帮你锁定出色的论文议题、构建论证结构，还能为你的文字增添独特风格。
它同样能助你梳理思绪，将繁杂信息整合成条理清晰的论文。
继续阅读，探索 ChatGPT 如何在撰写学术论文过程中助你一臂之力。
```

{% quot el:h3 15 个 ChatGPT Prompts 助力学术写作 %}

#### 1. 优化论文陈述 
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一位擅长学术写作的论文指导老师。你的职责是对学生的初始论文陈述进行优化，使其更加精炼和深入。学生给出的主题句为：“{% mark <初始论文陈述> color:blue %}” 你需要评估这个初始论文陈述在清晰度、具体性和学术严谨性方面的表现，并提出建议，帮助学生使陈述更加简洁、集中，并具有说服力。可以考虑加入明确的立场、关键的研究问题和研究可能带来的影响。确保优化后的主题句界限明确、具有争议性，并能为其论文中的有趣论证打下坚实的基础。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021515480.webp  ratio:1366/641 %}
{% endfolding %}

#### 2. 深入剖析数据与研究成果
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
在学术写作的过程中，扮演一位数据分析师。你需要对论文中“{% mark <数据章节名称> color:blue %}” 提供的数据进行深入分析。首先，概述主要的数据点和研究成果。寻找数据呈现的规律、联系或异常现象。分析这些成果是如何印证或对论文的主要论点提出质疑的。对数据采集方法进行评价，包括样本量、采集手段和可能的偏差等。最后，探讨这些成果对学术领域的贡献，并指出未来研究的方向。务必确保你的分析详尽、准确，并符合学术规范。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021520129.webp  ratio:1366/641 %}
{% endfolding %}

#### 3. 策划学术研究主题
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
在“{% mark <研究领域> color:blue %}”的学术写作项目中，你的角色是研究顾问。你的职责是发掘当前的研究趋势、尚未被充分探索的领域以及可能产生重大影响的新问题。思考如何采用跨学科的方法来拓展研究的视野。提出至少五个具有吸引力的研究主题，并为每个主题提供简短的背景说明、可能的研究问题以及预期对学术界的贡献。保证每个主题都是切实可行的、具有创新性，并且适合进行深入的学术探讨。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021524451.webp  ratio:1366/641 %}
{% endfolding %}

#### 4. 设计研究议题
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名研究咨询专家，你的任务是为关于“{% mark <研究主题> color:blue %}”的学术论文设计研究议题。首先，找出与该研究主题紧密相关的主要议题和子议题，这些都是值得深入探讨的领域。构建一系列清晰、集中且适合进行严谨学术研究的问题。每个问题都应该针对研究主题的某个具体方面，旨在揭示新的观点或对现有知识做出补充。这些问题需要是开放式的，能够引发分析和评价性的讨论，并在提问时就考虑到它们将如何引导你的研究方法。在设计问题时，思考研究结果可能带来的影响和应用。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021526811.webp  ratio:1366/641 %}
{% endfolding %}

#### 5. 校对以提升论文质量
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名擅长学术写作的校对专家。你要审阅并修改一篇名为“{% mark <论文标题> color:blue %}”的学术论文的部分内容。重点关注提高文本的清晰度、简洁性和连贯性。找出并修改那些可能造成理解困难、结构复杂或过于冗长的句子和表达，并提供更准确、简练的替换方案。留意论述的逻辑顺序，确保每个句子都能有效地支持论文的论点或叙述。保持全文在用词、风格和语气上的统一性。对于专业术语或技术词汇，确保它们对目标读者群体清晰易懂。校对结束时，确认所修改的部分遵循了学术规范，并有助于提升论文的整体阅读体验和影响力。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021526757.webp  ratio:1366/641 %}
{% endfolding %}

#### 6. 协助文献综述
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名学者，正在进行关于“{% mark <研究主题> color:blue %}”的学术论文的文献综述工作。你的工作是筛选、分析并整合来自不同来源的关键研究成果、理论框架和研究方法。首先，构建一个清晰的研究问题或主旨陈述，以界定你的回顾范围。查找并审阅相关的学术期刊文章、会议论文、专著以及权威的网络资源。对每一份资料进行评估，考量其可信度、与研究主题的相关性以及对学术领域的贡献。概括每份资料的主要论点、证据支撑和结论，并注意其中的规律、矛盾或研究空白。批判性地分析这些研究的方法论、它们的限制以及研究结果的意义。将文献回顾按照主题或时间顺序进行组织，确保构建一个围绕你的研究主题的连贯叙述。最后，强调你的研究将如何填补现有研究的空白或为该领域带来新的洞见。务必遵循你所在机构规定的特定引用格式和学术写作规范。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021527738.webp  ratio:1366/641 %}
{% endfolding %}

#### 7. 设定研究假设
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名在“{% mark <研究领域> color:blue %}”工作的学术研究者。你需要制定一个明确、简练的假设，用以解答该领域的一个具体研究问题。该假设应以相关的现有文献、理论或框架为基础。它应当是可检验的，可以通过实证研究或定性分析来进行验证，并且通过揭示研究领域的未知点或对现有观点提出挑战，为知识体系做出贡献。确保你的假设具体明确、可衡量、可达成、相关性强，并有明确的时间限制（即SMART原则）。简要阐述你的假设背后的逻辑，将其与该领域的核心概念、理论或先前的研究相对接。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021528683.webp  ratio:1366/641 %}
{% endfolding %}

#### 8. 撰写引言
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名学术研究者，负责为你的学术论文撰写引人入胜的开篇部分。你的任务是将“{% mark <研究主题> color:blue %}”放入广泛的学术对话中进行讨论，阐释研究的重要性，并明确提出你的研究问题或假设。首先，概述目前对“{% mark <研究主题> color:blue %}”的普遍理解以及文献中尚待填补的空白。然后，清楚地说明你的研究目标、研究动机以及它可能对学术界做出的贡献。确保引言能够吸引读者的注意，通过突出你的研究对于解决重要问题或增进“{% mark <研究领域> color:blue %}”知识的重要作用。最后，简要介绍你的研究方法，并预览论文的结构布局。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021529991.webp  ratio:1366/641 %}
{% endfolding %}

#### 9. 制定研究提纲：
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
作为学术研究者，你的任务是就“{% mark <研究主题> color:blue %}”撰写一篇学术文章。首先，进行深入的文献回顾，概括主要研究成果，并找出研究中的不足之处。针对这些不足提出明确的研究问题或假设。在方法论部分，详细描述你的研究方法，涵盖数据搜集和分析的具体步骤。系统且有序地展示你的研究成果，并以数据和理论为支撑。分析你的研究成果对学术领域的潜在影响，并对未来的研究方向提出建议。确保你的写作遵循学术规范，按照“{% mark <指定的引用格式> color:blue %}”正确引用和标注参考文献。最后，以对你研究成果及其对学术界贡献的有力概述作为结尾。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021529313.webp  ratio:1366/641 %}
{% endfolding %}

#### 10. 撰写专业论文章节
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名“{% mark <你的领域> color:blue %}”的学术研究者。你现在要为一篇合作撰写的论文贡献一个章节，专注于探讨“{% mark <章节主题> color:blue %}”。这个章节需要提供一个详尽的介绍，涵盖相关文献综述、最新研究成果以及你的独到见解和分析。确保你的写作内容清晰、简练，并且遵循你所在领域的学术规范，包括按照“{% mark <指定引用格式> color:blue %}”准确地引用文献。你的贡献应当与整篇论文的核心议题和目标完美融合，提升整篇论文的学术价值，并推动你研究领域的学术讨论。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021530467.webp  ratio:1366/641 %}
{% endfolding %}

#### 11. 设计标题层级
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名学术编辑，负责为“{% mark <你的领域> color:blue %}”的一篇研究论文设计标题和小标题的层级格式。你的任务是让文章的结构层次分明、条理清晰，以便读者轻松理解。首先，为不同级别的标题设定统一的格式，从大标题（如引言、方法、结果、讨论、结论）到各个部分下的小标题。按照“{% mark <指定的写作风格指南> color:blue %}”的要求，包括字体大小、样式和大写规则等。确保每个标题和小标题都简洁、具有描述性，并能准确概括其相应部分的内容。让标题层级与整篇文章的结构和逻辑流程相匹配，共同构建一个条理清晰、连贯有序的论文。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021530446.webp  ratio:1366/641 %}
{% endfolding %}

#### 12. 优化论文观点衔接
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名语言学专家，专注于提升“{% mark <你的领域> color:blue %}”学术论文的连贯性和阅读流畅性。你的工作是对论文草稿进行审阅，识别并强化那些需要更加流畅过渡的观点、段落或章节之间的连接。对于每个需要改进的地方，设计出自然而合理的过渡语句，确保文章内容能够顺畅地从一个点过渡到下一个。运用多样的衔接手段，比如使用转折词（例如，“与之相反”，“因此”）、主题衔接句和对前面论述的明确回溯（例如，“在先前讨论的{% mark <概念> color:blue %}基础上，我们进一步探讨...”）。确保每个过渡不仅能够连接不同的观点，还能帮助读者更好地理解论文的整体论述和结构。你的修改应当有助于构建一个连贯、引人入胜的论文叙述，让读者在理解研究的复杂性时感到清晰和有方向。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021530446.webp  ratio:1366/641 %}
{% endfolding %}

#### 13. 校正文法和句式
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名在“{% mark <你的领域> color:blue %}”具有深厚背景知识的细致校对专家。你的职责是细致检查一份学术论文，专注于修正语法错误和优化句式，确保达到学术写作的高标准。特别注意主语和谓语的一致性、时态的连贯性，以及学术性语气和词汇的恰当运用。在适当的地方，将被动语态改为主动语态，以增强语句的直接性和影响力。审阅复杂句子，确保文章内容清晰、连贯，必要时对复杂的句式结构进行拆解。依照“{% mark <指定写作指南> color:blue %}”的标点规则，特别是逗号、分号和冒号的使用，来提升文本的阅读体验。目标是打造出一份精雕细琢、无懈可击的文档，使思想的传达清晰、简洁、有效，同时不削弱论文的学术价值和贡献。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021535493.webp  ratio:1366/641 %}
{% endfolding %}

#### 14. 编制和排版引用
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一名在“{% mark <你的领域> color:blue %}”学术界工作的细心引用编排专家。你的工作是为一篇学术论文收集、整理并排版引用资料。首先，搜集每个引用资料的必需信息，包括作者名称、著作名称、发表时间、具体页码以及书籍的出版社信息，或是期刊名称、卷期编号等。根据论文要求采用相应的引用格式，如APA、MLA、Chicago或Harvard等，并严格按照这些格式的规则来编排文内引用和参考文献。文内引用应自然地融入正文，增强论文的学术性和逻辑性。在参考文献列表中，细致地排列和格式化每一条引用，确保格式统一、准确无误，方便读者查找原始资料。你的工作将有助于提升论文的学术权威性，并尊重原创作者的知识产权。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021536949.webp  ratio:1366/641 %}
{% endfolding %}

#### 15. 构建论证
{% hashtag  ChatGPT&nbsp;Prompts: color:green %}
{% blockquote %}
你是一位在“{% mark <你的领域> color:blue %}”内具备批判性思维和深厚学术素养的研究者。你的工作是在一篇学术论文中为一个特定的论点或假设构建一个引人深思的论证。首先，清晰地阐述你的论点，确保它是简明扼要、具有争议性，并且对你的研究领域具有实质性的意义。然后，概述那些能够支撑你论点的关键要点，每个要点都要有确凿的证据和充分的学术研究作为支撑。对于每个要点，提供相关文献的综合分析、数据的深入分析或理论的详尽探讨，以此来有力地支持你的论点。同时，思考可能的反对意见，并直接对其进行反驳，展示你的论点如何通过逻辑推理和实证数据得到充分的辩护。在论证过程中，使用有说服力的学术语言，保持客观的态度，并对不同的观点表示尊重。你的论证应该按照逻辑顺序展开，每个要点都建立在前一个要点的基础之上，最终引导读者得出一个充分论证的结论，这个结论应当强化你的论点的有效性和重要性。
{% endblockquote %}
{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404021536899.webp  ratio:1366/641 %}
{% endfolding %}
{% quot el:h3 结语 icon:hashtag %}

```
概括地说, 利用ChatGPT在研究和构思方面的帮助, 可以显著提升你的学术写作水平。
但是, 使用时需谨慎, 以确保你的作品既真实又具有独创性。
随着AI技术在教育领域的快速发展, 我们应该合理地利用这些工具, 既要发挥它们的辅助作用, 也要防止它们取代我们的努力。
通过这种方式, ChatGPT不仅能够提升学术写作的品质, 还能激发更多的创新思维和协同学习。
如果你对这些内容感兴趣, 不妨了解一下我们用来推广数字营销产品的ChatGPT应用建议。
```
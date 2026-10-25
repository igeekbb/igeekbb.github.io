---
cover: https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404081036057.webp
collection:
  profile: topic
  id: prompts
title: 转译-7个必备的 ChatGPT Excel Prompts
date: 2024-04-04 10:39:28
tags: [ChatGPT, Prompt]
categories: [AI] 
---
{% quot el:h3 引言 icon:hashtag %}

{% box color:cyan %}
[7 Essential ChatGPT Prompts for Excel ](https://www.godofprompt.ai/blog/7-essential-chatgpt-prompts-for-excel-the-only-you-will-ever-need) 主要介绍了如何通过ChatGPT来简化和提高Excel操作的效率,帮助用户解决各种Excel任务。
{% endbox %}

{% poetry 本文用到的工具们 footer:我认为一个好的&nbsp;Prompts&nbsp;可以一定程度弥补国产大模型的不足 %}
- 月之暗面 moonshot 国产大模型 {% button Kimi https://kimi.moonshot.cn/ size:xs %}.

- 通过 {% button kimi-free-api https://github.com/LLM-Red-Team/kimi-free-api/ size:xs %} 转为 API.
- 在 [Open WebUI](https://github.com/open-webui/open-webui) 使用 {% button 宝玉翻译 https://x.com/geekbb/status/1737634536257995177?s=20 size:xs %} Prompts .
- {% mark 全文翻译采用'意译',仅修改几处,感谢&nbsp;AI&nbsp;工具辛勤付出. color:orange %}
- 所有对话保存在"[chat-7个必备的 ChatGPT Excel 指令.txt](https://github.com/igeekbb/OSS/blob/main/appendix/chat-%E6%8E%8C%E6%8F%A1%20Excel%20%E6%98%AF%E5%BD%93%E4%BB%8A%E8%81%8C%E5%9C%BA%E5%BF%85%E5%A4%87%E7%9A%84%E5%85%B3%E9%94%AE%E8%83%BD%E5%8A%9B.txt)",有兴趣可以自行查看.
{% endpoetry %}

{% quot el:h3 正文 icon:hashtag %}

```
在当今职场，熟练掌握 Excel 是极其重要的技能。就算是资深专家，也会偶尔遇到一些复杂的难题，影响他们的工作效率。
如果我们告诉你，通过ChatGPT可以解决你所有的Excel问题，你会怎么想呢？
我们将向你展示6个非常实用的 ChatGPT 技巧，它们能够有效地显著提高你的工作效率。
同时，我们还会向你介绍如何让 ChatGPT 成为你处理 Excel 工作的有效工具。
```

{% quot el:h3 7个必备的 ChatGPT Excel 指令 %}

#### 1.理解 Excel 函数
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 当你需要了解某个 Excel 函数是如何工作的时候，可以使用以下格式向 ChatGPT 提问：
{% blockquote %}
请详细解释 Excel 中“{% mark <函数名称> color:blue %}”的工作原理，并且分步骤说明。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071906442.webp  ratio:1750/1730 %}
{% endfolding %}
 
#### 2.如何使用 Excel 函数
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 通过以下提问示例，我们将创建一个简洁的指南，帮助你掌握如何使用任何 Excel 函数：
{% blockquote %}
如何利用Excel的“{% mark <函数名称> color:blue %}”来“{% mark <实现特定目的> color:blue %}”？请提供分步指导，跳过基础步骤。
{% endblockquote %}

例如，我们将通过一个实例来学习如何计算一组单元格的平均值。
{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071907761.webp  ratio:1500/942 %}
{% endfolding %}

#### 3.创建 Excel 命令
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 有时，你可能需要快速创建一个 Excel 命令。幸运的是，ChatGPT 可以协助你完成这项任务。使用以下提示模板来请求任何 Excel 命令：
{% blockquote %}
请编写一个用于完成“{% mark <具体任务描述> color:blue %}”的 Excel 命令。请直接给出代码。
{% endblockquote %}
只需清晰地描述你希望在Excel中完成的任务，ChatGPT便会为你提供相应的命令代码。
{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071907241.webp  ratio:1660/498 %}
{% endfolding %}

#### 4.生成宏命令
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 对于热衷于Excel自动化功能的用户来说，宏是一个非常强大的工具值得深入了解。ChatGPT 为你提供支持，帮助你学习如何高效地创建和运用宏。
根据 Microsoft 的官方定义，宏是你能够进行多次重复执行的动作或一系列动作。创建宏基本上就是记录下你的鼠标操作和键盘输入，以此来实现任务的自动化。
下面，我为你准备了一个提问示例，以便你在编写宏时得到帮助：
{% blockquote %}
编写一个VBA Excel宏，用于“{% mark <执行特定操作> color:blue %}”,请直接提供代码。
{% endblockquote %}
我曾尝试编写一个基础宏，它的功能是从单元格中提取数值，并根据这个数值打开相应的工作表。
{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071907049.webp  ratio:1692/1122 %}
{% endfolding %}

#### 5.在 Excel 中执行复杂任务
{% hashtag  ChatGPT&nbsp;Prompts color:green %} Excel 不仅仅是用来完成基本任务的；它还可以处理包括数据分析和图表创建在内的复杂工作。ChatGPT 帮助你完成这些困难任务,清晰地描述你想要做什么，包括每一个细节。
{% blockquote %}
充当一个熟练的Excel助手,“{% mark <阐述任务的具体内容> color:blue %}”
{% endblockquote %}

我已经得到了如何执行每一步的指导，并且对每个步骤都有清晰的理解。
{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071908447.webp  ratio:1652/1716 %}
{% endfolding %}

#### 6.让 ChatGPT 成为 Excel 助手
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 在 Excel 中为每项任务设置单独的提示可能会让人感到繁琐。其实，你可以通过一个统一的提示，让 ChatGPT 成为你处理任何 Excel 任务的得力助手。
下面是一个能让 ChatGPT 像 Excel 专家那样提供帮助的通用提示：

{% blockquote %}
作为一个 Excel 专家，为完成 Excel 中的特定任务提供详细的逐步指导。这可能包括创建数据透视表、数据格式化、运用公式或函数、绘制图表或图形，以及其他各种 Excel 相关任务。请对每一步进行详尽的解释，明确指出必要的配置或选择，阐释应使用的函数，并给出技巧和建议，以保证任务能够准确且高效地完成。
请协助我完成以下任务：“{% mark <具体描述你的任务> color:blue %}”
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071908698.webp  ratio:1624/1754 %}
{% endfolding %}

#### 7.将 ChatGPT 变成一个 Excel 表格
{% hashtag  ChatGPT&nbsp;Prompts color:green %} 实际上，你可以将 GPT 作为一个 Excel 表格的文本版来使用，它会根据你的指令进行数据转换或计算。
{% blockquote %}
请作为一个基于文本的 Excel 表格与我互动。你只需以文本形式回复一个包含行号和列标（从A至L）的10行空白 Excel 表格。第一列应留空，用于标注行号。我会指示你哪些内容需要填入单元格，而你的回复应当仅为 Excel 表格的文本结果，无需其他内容。请避免提供解释性文字。如果需要进行计算，我会给出相应的公式，你执行后，请仅以文本形式回复计算后的 Excel 表格结果。首先，请给我一个空白的表格模板。
{% endblockquote %}

{% folding child:codeblock open:false  ChatGPT&nbsp;Response: %}
{% image https://cdn.jsdelivr.net/gh/igeekbb/OSS@main/2024/202404071909084.webp  ratio:1634/1216 %}
{% endfolding %}

{% quot el:h3 结语 icon:hashtag %}

```
总的来说，ChatGPT 是一个非常实用的工具，能够有效协助你完成多种类型的 Excel 任务。
并不像大家想象的那样，使用 ChatGPT 处理 Excel 不需要很多的提示；几个有效准备的提示就足以应对。
通过今天向你介绍的七个 Excel 提示生成器，你现在已经具备了应对可能出现的不同 Excel 挑战的能力。
```
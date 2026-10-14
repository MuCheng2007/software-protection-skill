# 案例索引与证据等级

20条是候选资料数量，包含排除记录，不是确认破解软件数量。所有记录当前均未由本项目独立复现。

| ID | 日期 | 来源 | 类型 | 摘要与局限 |
| --- | --- | --- | --- | --- |
| C01 | 2026-10-03 | [看雪 · 基于 VMProtect授权锁架构的RSA算法另类Bypass思路](https://bbs.kanxue.com/thread-293138.htm) | `author_demo` | 作者用自制样例展示运行时参数篡改；依赖已知目标 ProductCode。 作者自制授权锁样例，不计为商业软件实战；仅公开正文核对，未独立复现，不推广到全部RSA或当前版本。 |
| C02 | 2026-07-23 | [看雪 · 1.13.7Typora离线授权逆向](https://bbs.kanxue.com/thread-292131.htm) | `author_report` | 作者报告分析字节码后替换本地密码处理与完整性读取行为。 结论限该文所述版本；截图未逐张验证。列表日期与正文发布日期不同，以正文为准。 |
| C03 | 2026-09-14 | [看雪 · 逆向 HanaAgent：一次 Electron 组件自还原机制的定位与禁用](https://bbs.kanxue.com/thread-292945.htm) | `adjacent_tamper_report` | 作者修改本地组件与引导逻辑，并区分归档哈希校验和组件恢复机制。 开源组件行为修改，不是付费授权被破解；不计入授权破解数量。 |
| C04 | 2026-09-04 | [看雪 · 某FPS外挂网络验证分析与网络验证服务端API的漏洞](https://bbs.kanxue.com/thread-292855.htm) | `author_report` | 作者报告替换客户端授权配置并接入另一软件位；讨论后台字段可修改问题。 只抽象授权失效机制，不提供作弊功能。作者对跨软件位冲突的推测未测试，不能认定服务器越权。 |
| C05 | 2026-09-14 | [看雪 · HTTP Debugger Pro 破解简单的网络验证程序](https://bbs.kanxue.com/thread-292949.htm) | `hypothetical_tutorial` | 用设想的请求响应说明只信成功字段的风险。 没有可核对目标及实际成功记录，不能计为真实破解案例。 |
| C06 | 2026-09-15 | [看雪 · KCTF 第一题（AliCrackme_1 逆向分析过程）](https://bbs.kanxue.com/thread-292960.htm) | `ctf_teaching` | 教学样例通过资源中的可逆查表和本地比较完成校验，日志提供线索。 绝对日期来自搜索摘要和正文路径，部分抓取显示相对日期，日期精度需保留此冲突；不是商业案例。 |
| C07 | 2026-05-27 | [看雪 · vofa 注册认证逆向分析与破解实战](https://bbs.kanxue.com/thread-291357.htm) | `historical_author_report` | 正文描述定位公钥与本地授权判断后修改执行结果。 时间窗外补充；对话式作者叙述不等于独立复现或厂商确认。 |
| C08 | 2026-03-21 | [看雪 · AIDA64 8.25.8200 Business 逆向工程与Keygen实战](https://bbs.kanxue.com/thread-290437.htm) | `historical_author_report` | 可读正文讨论本地序列号规则与校验算法恢复。 正文提示登录可看完整内容；未下载附件。列表近期回复不代表近期发表。 |
| C09 | 2025-01-01 | [看雪 · VMProtect本地授权锁的分析与破解(基于Q*量子网络验证例子)](https://bbs.kanxue.com/thread-285076.htm) | `historical_author_report` | 作者在样例中讨论替换本地信任参数或解密结果的共同瓶颈。 历史资料；正文明确不分析平台网络验证。不能当作该平台完整服务被攻破。 |
| C10 | 2022-01-01 | [吾爱汇编 · 绕过.NET(C#)类库的简易校验](https://www.52hb.com/thread-53818-1-1.html) | `historical_partial` | 可读部分列出托管程序集分析背景，关键内容要求回复后查看。 未取得完整机制，不用于新增具体规则；没有登录或回复解锁。 |
| C11 | 2023-03-01 | [吾爱汇编 · 新手某UPX壳脚本，脱壳+破简单网络验证+心跳处理](https://www.52hb.com/thread-58093-1-1.html) | `historical_partial` | 可读部分讨论压缩壳分析，授权与心跳后续内容隐藏。 标题不证明具体机制和成功；不计为近期心跳破解证据。 |
| C12 | 2026-06-23 | [看雪 · 软件安全保卫战：从“加壳自欺”到“云端降维”，2026年开发者必须掌握的新型网络验证体系](https://bbs.kanxue.com/thread-291758.htm) | `excluded_opinion` | 泛化防护观点文章。 无本轮可核对实测链，不纳入失效机制证据。 |
| C13 | 2026-05-07 | [看雪 · 从“联网傀儡”到“核心掌控”：2026年软件验证的自救与私有化部署实战](https://bbs.kanxue.com/thread-291130.htm) | `excluded_opinion` | 私有化部署观点与推广性主张。 不作为免费、绝对强防护或具体破解效果的依据。 |
| C14 | 未核实 | [看雪 · Jetbrains激活Discover Server实现的分析](https://bbs.kanxue.com/thread-283941.htm) | `unclassified_excluded` | 论坛列表发现，打开但未完成正文机制及日期分析。 不得从标题补写方法或作为近期案例。 |
| C15 | 未核实 | [看雪 · 【安装 破解】IDA Pro 9.4sp1 9月15更新版](https://bbs.kanxue.com/thread-293045-19.htm) | `excluded_distribution` | 检索返回下载分发帖的回复分页。 不分析、不下载；没有机制证据，分页显示日期不作为原帖日期。 |
| C16 | 2026-06-20 | [飘云阁 · AnyGo 8.3.x 算法分析记录初稿](https://www.chinapyg.com/thread-167556-1-1.html) | `historical_author_report` | 作者报告极短 RSA 模数、模拟验证响应，以及启动时信任本地保存状态的多条路径。 时间窗外补充；自动化脚本隐藏且功能未长期测试，作者自己也保留其他检查存在的可能；未独立复现。 |
| C17 | 2026-08-04 | [飘云阁 · [实战] 我破我自己：3层防御，防了个寂寞](https://www.chinapyg.com/thread-168526-1-1.html) | `ctf_teaching` | 自制 Android 样例展示硬编码、可逆编码、无效混淆及本地判断替换；同时暴露敏感调试日志。 本轮经正常浏览器读取正文，确认首次发表20:56。教学样例不是商业软件破解；原文防御建议并非都可靠，已单独审查。 |
| C18 | 2026-08-04 | [飘云阁 · 初高中——考务助手【全自动AI破解启示】3天内免费算永久码](https://www.chinapyg.com/thread-168527-1-1.html) | `author_report_limited_detail` | 作者自述移除考务助手 xlsm 的 VBA 授权相关模块并修复调用后使用，未公布完整修改轨迹。 本轮经浏览器确认首次发表22:23；仅支持可编辑本地业务绕过的审查线索，不能断言服务器或密码算法被攻破。未下载收费附件。 |
| C19 | 2026-09-03 | [飘云阁 · 易用宝单机版V2.10.2218.2026 商业版+ 离线激活注册机](https://www.chinapyg.com/thread-169102-1-1.html) | `author_instructions_limited_detail` | 作者说明通过替换公钥并从离线申请提取设备信息，随后写入授权配置；无完整反汇编轨迹。 本轮浏览器读取完整公开说明，首次发表13:36；升级为有方法说明的作者主张，未验证工具实现或实际运行。不能推断只改配置即可绕过。 |
| C20 | 2026-09-07 | [飘云阁 · XX周易系列安卓版注册机算号分享](https://www.chinapyg.com/thread-169167-1-1.html) | `excluded_key_sharing` | 正文只说明提供算号，未披露注册算法或分析过程。 有日期和正文不代表有方法证据；没有保存回复中的机器码、用户信息或激活码。 |

类型说明：author_demo/ctf_teaching为自制教学；author_report为作者实践主张；limited_detail表示细节有限；historical为时间窗外补充；excluded为不用于具体机制结论的记录。adjacent_tamper_report是相邻篡改研究，并非授权破解。

[结构化原始记录](../skills/software-protection/references/forum-cases.json) · [调研范围](research/forum-research-coverage.json) · [维护方法](../skills/software-protection/references/research-method.md)

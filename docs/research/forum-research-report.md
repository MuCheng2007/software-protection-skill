# 国内公开逆向案例调研与 skill 加固记录

首轮：2026-10-14；飘云阁补充：2026-10-15。首轮时间窗：2026-07-16 至 2026-10-14；补充窗口：2026-07-17 至 2026-10-15。

## 覆盖与完成程度

本轮完成有限公开检索、原帖筛选、简短证据记录和 skill 更新，没有完成或声称完成“近期全部数据拉取”。保存的是原创摘要与来源，不是全文镜像。搜索工具可能提供旧缓存；论坛列表日期常是最近回复，已优先核对正文。

累计记录20条候选。可用于近期分层分析的材料现为9条：原有6条（其中VMP/RSA为自制样例），加上飘云阁两篇近期软件方法说明和一篇近期自制教学样例；它们均为作者陈述或教学，未独立复现。另有算号/分发、历史、部分正文及排除记录，不能作为近期技术破解数量。

看雪提供首轮可读案例。吾爱破解仍存在读取缺口，纳入0条并不代表该站没有相关内容。吾爱汇编与吾爱破解是不同站点。

飘云阁在补充轮通过正常浏览器读取成功，已核对软件逆向与移动安全列表，并读取C17–C20正文；此前仅摘要的C17/C18、仅分发判断的C19现已更正。C18/C19有方法说明但没有完整分析链，C17是教学，C20没有方法。C16仍为窗外历史补充。未进行登录、回复解锁、付费、附件下载或样本执行。

因此不能给出国内论坛整体破解频率、方式占比、热门排行或各保护产品胜负结论。案例的作者主张不代表当前版本仍然受影响。

## 从材料得出的有限结论

- 密码学验签和客户端执行可信是不同问题。C01、C02 提示需要检查参数、信任锚、函数结果与后续使用链，不只看算法名称。
- C04 提示客户端初始化配置、响应来源和授权后台字段约束需要一起审查。作者未验证的跨软件位推测不升级成服务器越权结论。
- C03 提示检查实际加载文件与更新/恢复链；该案例是组件行为修改，不列为付费破解。
- C05 是场景设想，C06 是教学样例；它们只提供检查线索。
- 历史补充 C07–C09 用于补齐本地规则恢复和共享授权瓶颈，不算“最近新出现的方法”。

## 已修改技能

新增 failure-patterns.md，将线索转成十一类检查：密码执行链篡改、服务信任替换、可推导发卡规则、打包误作保密、加载/更新完整性缺口、共享授权瓶颈、后台权限/字段约束、生命周期回归、重启恢复路径漏验、密码参数强度不足、可编辑宏/脚本授权调用被移除。每类包含适用前提、控制、验收与限制。第八类是工程回归建议，本轮没有足够近期样本证明流行程度。

飘云阁历史C16补齐恢复路径和参数强度检查；补充轮近期C18促成F11宏/脚本执行边界审查，C19加强F01信任公钥替换与F09恢复配置检查，C17加强日志及可逆编码审查。具体结论、证据局限及官方资料见 chinapyg-supplement-report.md。没有将作者主张升级为已确认漏洞或已复现成功。

SKILL.md 已接入失效模式和调研维护流程；acceptance-and-delivery.md 已补充场景。forum-cases.json 保存每条证据范围与未复现状态，research-method.md 要求未来增量更新保持去重、日期核对和证据分级。

Electron 专项建议根据官方 [ASAR integrity](https://www.electronjs.org/docs/latest/tutorial/asar-integrity) 与 [fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) 文档核对：适配目标版本，配套考虑完整性与限定加载路径，在签名前配置并测试兼容性。不把代码签名存在等同于所有设备强制阻止修改。

## 来源索引

| ID | 原帖日期 | 类型 | 读取范围 | 来源 |
| --- | --- | --- | --- | --- |
| C01 | 2026-10-03 | author_report | public_body | [基于 VMProtect授权锁架构的RSA算法另类Bypass思路](https://bbs.kanxue.com/thread-293138.htm) |
| C02 | 2026-07-23 | author_report | public_body | [1.13.7Typora离线授权逆向](https://bbs.kanxue.com/thread-292131.htm) |
| C03 | 2026-09-14 | adjacent_tamper_report | public_body | [逆向 HanaAgent：一次 Electron 组件自还原机制的定位与禁用](https://bbs.kanxue.com/thread-292945.htm) |
| C04 | 2026-09-04 | author_report | public_body | [某FPS外挂网络验证分析与网络验证服务端API的漏洞](https://bbs.kanxue.com/thread-292855.htm) |
| C05 | 2026-09-14 | hypothetical_tutorial | public_body | [HTTP Debugger Pro 破解简单的网络验证程序](https://bbs.kanxue.com/thread-292949.htm) |
| C06 | 2026-09-15 | ctf_teaching | public_body | [KCTF 第一题（AliCrackme_1 逆向分析过程）](https://bbs.kanxue.com/thread-292960.htm) |
| C07 | 2026-05-27 | historical_author_report | public_body | [vofa 注册认证逆向分析与破解实战](https://bbs.kanxue.com/thread-291357.htm) |
| C08 | 2026-03-21 | historical_author_report | public_partial | [AIDA64 8.25.8200 Business 逆向工程与Keygen实战](https://bbs.kanxue.com/thread-290437.htm) |
| C09 | 2025-01-01 | historical_author_report | public_body | [VMProtect本地授权锁的分析与破解(基于Q*量子网络验证例子)](https://bbs.kanxue.com/thread-285076.htm) |
| C10 | 2022-01-01 | historical_partial | public_partial_hidden | [绕过.NET(C#)类库的简易校验](https://www.52hb.com/thread-53818-1-1.html) |
| C11 | 2023-03-01 | historical_partial | public_partial_hidden | [新手某UPX壳脚本，脱壳+破简单网络验证+心跳处理](https://www.52hb.com/thread-58093-1-1.html) |
| C12 | 2026-06-23 | excluded_opinion | search_excerpt | [软件安全保卫战：从“加壳自欺”到“云端降维”，2026年开发者必须掌握的新型网络验证体系](https://bbs.kanxue.com/thread-291758.htm) |
| C13 | 2026-05-07 | excluded_opinion | search_excerpt | [从“联网傀儡”到“核心掌控”：2026年软件验证的自救与私有化部署实战](https://bbs.kanxue.com/thread-291130.htm) |
| C14 | 未核实 | unclassified_excluded | page_opened_not_analyzed | [Jetbrains激活Discover Server实现的分析](https://bbs.kanxue.com/thread-283941.htm) |
| C15 | 未核实 | excluded_distribution | reply_page_excerpt | [【安装 破解】IDA Pro 9.4sp1 9月15更新版](https://bbs.kanxue.com/thread-293045-19.htm) |
| C16 | 2026-06-20 | historical_author_report | public_partial_hidden | [AnyGo 8.3.x 算法分析记录初稿](https://www.chinapyg.com/thread-167556-1-1.html) |
| C17 | 2026-08-04 | ctf_teaching | public_body_browser | [[实战] 我破我自己：3层防御，防了个寂寞](https://www.chinapyg.com/thread-168526-1-1.html) |
| C18 | 2026-08-04 | author_report_limited_detail | public_body_browser | [初高中——考务助手【全自动AI破解启示】3天内免费算永久码](https://www.chinapyg.com/thread-168527-1-1.html) |
| C19 | 2026-09-03 | author_instructions_limited_detail | public_body_browser | [易用宝单机版V2.10.2218.2026 商业版+ 离线激活注册机](https://www.chinapyg.com/thread-169102-1-1.html) |
| C20 | 2026-09-07 | excluded_key_sharing | public_body_browser | [XX周易系列安卓版注册机算号分享](https://www.chinapyg.com/thread-169167-1-1.html) |

## 后续补齐路径

如有吾爱破解的授权导出或可读帖子列表，可沿用同一记录格式离线去重、核对正文日期并继续补充；当前访问失败不应通过猜测填补。需要全量归档时还须明确板块、起止日期、合法可用获取方式、分页终点与完整性校验，单靠搜索结果不能证明全量。

## 验证边界

本轮只验证 skill 的结构、内部引用、案例记录一致性与压缩包完整性，没有真实目标程序、没有执行防破解测试，也没有部署授权服务。具体自动检查结果见 validation-result.json。

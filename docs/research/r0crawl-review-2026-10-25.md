# r0crawl_skills 工作流审查与防御提炼

审查日期：2026-10-25。来源项目：[manyuegong33/r0crawl_skills](https://github.com/manyuegong33/r0crawl_skills)，以发布账号标识来源，不推断真实姓名或其他模块的个人作者。固定提交：[b9eb545926ede5f24adeb0d7e60d97ee73b409f7](https://github.com/manyuegong33/r0crawl_skills/tree/b9eb545926ede5f24adeb0d7e60d97ee73b409f7)。

## 检查范围

本地514个文件的 Git blob SHA-1 与该提交完整树逐一一致。只读检查根入口、工具矩阵、证据约定、路由/重建流程、Python冻结程序及运行时模块、关键脚本和模板；未运行附带脚本，也未用其分析第三方目标。未逐条验证所有模块的技术正确性。

统计限定：skills/ 的一级子目录中共218个 SKILL.md。按 UTF-8-SIG 读取，移除开头 YAML frontmatter 和首个一级标题后，余文 strip；得到24种不同正文，最大相同正文组170个。这个统计只衡量文本重复，不评价作者能力，也不预测真实任务成功率。

## 可定位的一手依据

- [根入口与路由](https://github.com/manyuegong33/r0crawl_skills/blob/b9eb545926ede5f24adeb0d7e60d97ee73b409f7/SKILL.md)：按目标选择材料及分析路线。
- [分析转向规则](https://github.com/manyuegong33/r0crawl_skills/blob/b9eb545926ede5f24adeb0d7e60d97ee73b409f7/skills/ctf-reverse-pivot-control/SKILL.md)：分层定位、竞争假设与根据证据换路线。
- [冻结 Python 程序](https://github.com/manyuegong33/r0crawl_skills/blob/b9eb545926ede5f24adeb0d7e60d97ee73b409f7/skills/python-frozen-app-reversing/SKILL.md)：检查入口以外的运行组件。
- [CPython 运行时](https://github.com/manyuegong33/r0crawl_skills/blob/b9eb545926ede5f24adeb0d7e60d97ee73b409f7/skills/cpython-runtime-introspection/SKILL.md)：围绕运行时语义边界取证。
- [虚拟化模块](https://github.com/manyuegong33/r0crawl_skills/blob/b9eb545926ede5f24adeb0d7e60d97ee73b409f7/skills/virtualization-protection/SKILL.md)：本版本是流程建议，不是通用去虚拟化实现。

## 本项目新增的防御推论

以下为维护方根据工作流作出的设计推论，不是来源作者作出的安全承诺：

1. 以实际执行层次及结果消费者识别保护位置，不依靠入口改名或假脚本。
2. 为核心数据记录出现位置、读取者、寿命和复用条件，检查最终发布材料；原生化和缩短明文寿命只改变暴露方式或成本。
3. 在一次合法运行、材料保存、本地结果替换及撤销后，用不同新任务验证提供方仍控制什么。
4. 服务端逐请求授权保护其能力；有效用户的代理、缓存、复制和缓慢提取需要单独评价，不能只测无卡密用户。

这些推论与 [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) 的授权执行原则配合使用；实际方案须由用户项目证据支持。

## 合并与排除

合并到 [AI逆向审查参考](../../skills/software-protection/references/ai-reverse-engineering.md)、技能入口和验收文档。没有复制第三方模块、脚本或研究全文，没有添加特定工具依赖；不把模板数量当能力数量，不声称防住该项目或证明其能破解某产品。

本轮属于工具工作流研究，不新增 C 系列案例，既有76条候选资料、12类模式、0次第三方样本运行复现不变。安装包只分发本项目原创技能内容与既有简短资料记录；第三方权利见 [NOTICE](../../NOTICE)。

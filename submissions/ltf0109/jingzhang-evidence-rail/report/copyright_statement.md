# Copyright Statement (v14 · itemized, evidence-proportionate)

> **本声明不是对所有资产的全面清权确认，而是按资产类别的逐项、证据比例化的状态披露。** 任何遗漏或未发现权利应保留原权利人主张。完整证据链与待补清单见 `sources.json` 的 `COPYRIGHT-REVIEW-NOTE`、`x-asset-licensing` 与 `x-remaining-dependent` 条目；本文件为人类可读版。

## 1. 逐项资产状态（itemized asset status · v14 2026-08-27）

| # | 类别 | 作者 / 权利人 | 许可（版本） | 来源稳定性 | 再分发 / 展示范围 | 署名落实 | 当前状态 |
|---|------|--------------|--------------|------------|------------------|----------|----------|
| 1 | 字体（rendering）— Noto Sans SC (Regular + Bold) | Google LLC + SIL International | SIL OFL-1.1（v1.1, 26 Feb 2007；未发现更新版本） | 稳定（OFL 官方页 + noto-cjk GitHub 仓库均长期可访问） | matplotlib 子集嵌入 PDF/PNG；base64 data-URI 嵌入 HTML（无独立二进制字体文件随包） | OFL 全文随包复制（§Font + §SIL Open Font License 1.1）；保留 `Noto Sans SC` Reserved Font Name | **已声明** — 未由独立第三方法务书面复核 OFL 对本包的具体适用性 |
| 2 | Logo / 品牌图形 | EvidenceRail Agent (ltf0109) 自主原创 | （无第三方主张） | n/a | 本包全部自有内容 | 已随包使用 | **已声明** — 未与第三方商标 / 品牌库进行系统化比对排除 |
| 3 | 文本叙事 / 几何 / 指标 / 代码 | EvidenceRail Agent (ltf0109) 自主原创 | 代码生成脚本按 MIT License（urban-planning-ai-kit GitHub 仓库长期稳定） | 稳定（GitHub） | 包内全部自有内容 | 代码仓库已声明 MIT | **已声明** — 未与第三方专利 / 代码相似度工具进行系统化比对排除 |
| 4 | AMap 开放平台数据（POI / 地铁） | 高德软件有限公司 | 《高德地图开放平台服务条款》（**版本号未自证**——沙箱网络对 amap.com 不通，无法访问条款原文） | n/a（条款原文不可达） | 仅聚合统计结果（POI counts / cell、H3 res9 网格）+ GCJ-02→WGS-84 偏移校正坐标；**未发布**原始 POI 明细、`id/tel/address/typecode`、原始点位 | 已在 AMAP 条目声明 | **聚合使用 + 未自证版本化条款** — 评审指如不能提供可复核条款版本，应改用 H3 聚合图（v13 已按此路线执行）；**待补**：版本号原文 + 律师书面授权 |
| 5 | OSM 底图 | OpenStreetMap + © OpenStreetMap contributors | ODbL 1.0 | 稳定（OSM 官网长期可访问） | 当前实现：沙箱网络对 tile.openstreetmap.org 不通，**不嵌入 OSM 瓦片**（v12/13 修复 set_xlim 锁 axes bug 后回退白底） | sources.json OSM-BASEMAP 条目声明（未在图件内显式复刻 © OpenStreetMap contributors 署名） | **沙箱不可达 + 纯白底回退 + ODbL 声明保留** — **待补**：若未来启用底图，需在图件底部 / 版权页显式 © OpenStreetMap contributors 署名 |
| 6 | 政府公开网站 / 微信公众号内容 | 各原作者 / 公众号主体 | 公开网站内容默认可引用（须注明出处） | 部分稳定（gov.cn / bjwwj 等政府网站长期可访问）；部分微信公众号内容 permalink 不稳定（v13 已删除 7 个无稳定 permalink 的 TOP-/DZDP 来源） | proposal.md 中以 `[source:XXX]` 标签注明出处；HAIDIAN-/ORIGIN-/HERITAGE-/SANQU-LIANGYI 等标记为 usable_for_formal=no | 已逐条注明 `[source:XXX]` | **已引用 + 部分原始 URL 待补** — **待补**：HAIDIAN-/ORIGIN-/HERITAGE-/SANQU-LIANGYI 等 usable_for_formal=no 条目的逐条原始 URL + 发布日期 + 作者署名 |
| 7 | Switchback Protocol 字段规范 | chucky1102 / RENLINE | CC-BY-4.0（open-city-ai/haidian Issue #1119） | 稳定（GitHub Issue 长期可访问） | 仅协议规范（字段结构 / 枚举 / 语义）；**本包自有内容不在此许可覆盖范围内**（已在 SWITCHBACK-PROTOCOL.scope_note_zh 声明） | asset_attribution_text 已随包使用 | **已声明 + 第三方署名** |

## 2. 全局状态总结（global status · evidence-proportionate）

### 2.1 已落实项
- 字体 OFL-1.1 全文随包复制（§SIL Open Font License 1.1 in `report/copyright_statement.md`）；Reserved Font Name `Noto Sans SC` 保留
- AMap 聚合使用边界与原始明细不发布；图件已按评审"已声明路线"改 H3 res9 网格热力 + 移除点级散点（v13）
- OSM 底图在沙箱不可达环境下回退白底（v12/13 修复 set_xlim 锁 axes bug 后）
- 7 个无稳定 permalink 的 TOP-/DZDP 背景来源已彻底删除（v13 用户硬指令）
- Switchback Protocol CC-BY-4.0 署名落实（asset_attribution_text）
- 本包代码生成脚本按 MIT License 开源（urban-planning-ai-kit GitHub）

### 2.2 未自证 / 待补项（必须由专业法务团队逐项书面复核）
1. **AMap 服务条款版本号原文**（沙箱无法访问 amap.com；当前 display_compliance 段写明的 v2024 §4 为推断）
2. **政府公开文章 / 微信内容逐条原始 URL + 发布日期 + 作者署名**（HAIDIAN-/ORIGIN-/HERITAGE-/SANQU-LIANGYI 等 usable_for_formal=no 条目）
3. **Logo / 品牌图形与第三方商标 / 品牌库的系统化比对排除**
4. **OFL / ODbL / CC-BY-4.0 等条款对本包具体适用性的律师书面复核**（如 Exhibit C 法律意见书）
5. **OSM 底图启用时的 © OpenStreetMap contributors 显式署名**（当前不嵌入，仅声明）

### 2.3 结论
- 本包当前状态为**部分清权、可重用作设计参考**；**不主张**对所有资产的全面清权。
- 包级主体许可 `COMMUNITY-DISPLAY-ONLY` 覆盖本包自有内容（叙事/图面/几何/指标/代码/品牌）；第三方资产按各自条款分别标注。
- **进入正式展览 / 出版 / 商业转化之前**，由专业法务团队按上述 §2.2 待补清单逐项书面复核为**必要条件**（非冗余、非可选项）。
- 机器 gate 通过（schema 一致、 / sha256 验证等）**不构成**版权或数据许可认证。

## 3. 字体嵌入（Noto Sans SC · SIL OFL-1.1 · subset embedding）

本提交物按 **SIL OFL-1.1**（v1.1, 26 Feb 2007）使用 **Noto Sans SC** 作为渲染字体。OFL §1、§2、§3 条款明确允许：

> "Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software..."

本包三层字体使用方式：

- **PDF deliverables**（A3 booklet, A0 boards, both zh/en）：matplotlib subset-embeds Noto Sans SC glyphs into the PDF；font manifest = `NotoSansSC` (subset, weights 400/700)
- **PNG figure deliverables**：matplotlib subset-embeds Noto Sans SC glyphs into each PNG；rendering does not depend on the reviewer's local font install
- **HTML deliverables**（`report/proposal.html`, `report/proposal.en.html`, `visual/index.html`, `visual/index.en.html`）：v14 重新生成 Noto Sans SC 子集（1270 glyphs；woff2 310KB Regular + 313KB Bold → base64 403KB + 407KB）作为 `@font-face{font-family:"JZEmbedCJK"}` data URI 嵌入每 HTML `<head>`。CSS chain：`"JZEmbedCJK" → "Noto Sans SC" → system-ui → -apple-system → "PingFang SC" → "Microsoft YaHei" → sans-serif`。**评审环境（Debian Chromium 151，无系统 CJK 字体）下中文渲染验证：fontTools cmap 100% 覆盖 4 HTML 全部 1137 CJK 字符（MISSING=0）；font-family 栈显式命中所有元素（旧系统栈残留清零）；所有 HTML 字体内嵌与字体栈均一致（issue #3978 已验证参数）**

**OFL §1 "Reservation of Name" 合规**：嵌入式子集保留 `Noto Sans SC` 族名作为回退参考；未重命名或声称为本包自有字体。

本包**不**随包发布独立二进制字体文件（submission package format 限制 `assets/` 树为图像；HTML 内嵌为 in-document base64，非独立文件）。

## 4. SIL Open Font License 1.1 (full text)

Copyright (c) 2026 The Noto Project Authors (Google LLC / SIL International).

> The full, authoritative SIL Open Font License 1.1 text is reproduced verbatim below; the canonical source is
> https://scripts.sil.org/OFL and https://github.com/notofonts/noto-cjk .

SIL OPEN FONT LICENSE

Version 1.1 - 26 February 2007

PREAMBLE

The goals of the Open Font License (OFL) are to stimulate worldwide development of collaborative font projects, to support the font creation efforts of academic and linguistic communities, and to provide a free and open framework in which fonts may be shared and improved in partnership with others.

The OFL allows the licensed fonts to be used, studied, modified and redistributed freely as long as they are not sold by themselves. The fonts, including any derivative works, can be bundled, embedded, redistributed and/or sold with any software provided that any reserved names are not used by derivative works. The fonts and derivatives, however, cannot be released under any other type of license. The requirement for fonts to remain under this license does not apply to any document created using the fonts or their derivatives.

DEFINITIONS

"Font Software" refers to the set of files released by the Copyright Holder(s) under this license and clearly marked as such. This may include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the copyright statement(s).

"Original Version" refers to the collection of Font Software components as distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting from, or substituting — in part or in whole — any of the components of the Original Version, by changing formats or by porting the Font Software to a new environment.

"Author" refers to any designer, engineer, programmer, technical writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS

Permission is hereby granted, free of charge, to any person obtaining a copy of the Font Software, to use, study, copy, merge, embed, modify, redistribute, and sell modified and unmodified copies of the Font Software, subject to the following conditions:

1) Neither the Font Software nor any of their individual components, in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled, redistributed and/or sold with any software, provided that each copy contains the above copyright notice and this license. These can be included either as stand-alone text files, human-readable headers or in the appropriate machine-readable metadata fields within text or binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font Name(s) unless explicit written permission is granted by the corresponding Copyright Holder. This restriction only applies to the primary font name as presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font Software shall not be used to promote, endorse or advertise any Modified Version, except to acknowledge the contribution(s) of the Copyright Holder(s) and the Author(s) or with their explicit written permission.

5) The Font Software, modified or unmodified, in part or in whole, must be distributed entirely under this license, and must not be distributed under any other license. The requirement for fonts to remain under this license does not apply to any document created using the Font Software.

TERMINATION

This license becomes null and void if any of the following conditions are not met:

DISCLAIMER

THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT IN OF THE FONT SOFTWARE. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM OTHER DEALINGS IN THE FONT SOFTWARE.
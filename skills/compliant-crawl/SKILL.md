---
name: compliant-crawl
description: >
  Thu thập dữ liệu web MỘT CÁCH TUÂN THỦ cho nghiên cứu: ưu tiên nguồn chính thống/
  mở/API, tôn trọng robots.txt và Terms of Service, không lấy dữ liệu cá nhân, giới
  hạn tần suất, ghi công nguồn, và xuất CSV kèm attribution để dùng/chia sẻ. Sử dụng
  khi người dùng muốn crawl/scrape, lấy số liệu tuyển sinh/thống kê từ portal trường,
  trang Bộ, cơ quan thống kê quốc gia, dữ liệu mở, hoặc cần bộ dữ liệu CSV có ghi công.
---

# Compliant data collection

Thu thập **dữ liệu công khai, dạng tổng hợp** cho nghiên cứu độc lập, **hợp pháp và có đạo đức**,
xuất **CSV kèm ghi công** để dùng và chia sẻ. Ưu tiên nguồn chính thống/mở trước khi crawl.

> Có bộ công cụ chạy thật kèm theo tại `C:\K3 Research\compliant-data-toolkit\`
> (`compliant_fetch.py`, `extract_tables.py`, `normalize.py`, `sources.csv`, `COMPLIANCE.md`, `CREDITS.md`).

## Đầu vào tối thiểu
Hỏi tối đa 3 câu: (1) Cần dữ liệu gì, đơn vị/năm nào? (2) Nguồn nào (portal trường / Bộ / thống kê QG / dữ liệu mở / báo chí)? (3) Kết quả dạng gì (CSV chia sẻ, hay chỉ tra cứu)?

## Nguyên tắc BẮT BUỘC (theo COMPLIANCE.md)
1. **Ưu tiên API/dữ liệu mở** (UNESCO UIS, World Bank, OECD, OpenAlex, data.gov.vn) — chỉ crawl khi không có API.
2. **Tôn trọng robots.txt** cho User-Agent của mình; bị Disallow thì **không lấy** (ví dụ `moet.gov.vn` chặn `/*.pdf$` → tải tay như con người, không để crawler cào).
3. **Tôn trọng ToS.** Site cấm scraping (nhiều báo) → **không cào**; báo chí chỉ dùng **đối chứng**, trích từng bài, có link.
4. **Không lấy PII** — chỉ số liệu tổng hợp (phổ điểm, đếm theo tổ hợp/ngành). Không điểm/tên/SBD cá nhân (Nghị định 13/2023).
5. **Chỉ trang công khai** — không vượt login/paywall/captcha.
6. **Lịch sự** — User-Agent có email liên hệ, tuân crawl-delay, rate-limit, retry hạn chế; không gây quá tải.
7. **Ghi công mọi số** — mỗi dòng dữ liệu mang source_id, URL, ngày truy cập, tier, license. CSV **không** ghi nếu thiếu attribution.
8. **Tôn trọng giấy phép khi tái dùng** — CC BY (World Bank), CC0 (OpenAlex), UIS terms… ghi công theo `CREDITS.md`.

## Quy trình
1. **Chọn nguồn** từ `sources.csv`; xác định tier + license + có API không.
2. **Nguồn mở/API trước:** tải trực tiếp; bỏ qua bước crawl.
3. **Portal trường:** `python compliant_fetch.py` để kiểm robots trước; chỉ fetch phần được phép.
4. **PDF bị robots chặn (MOET):** researcher **tải tay**, đưa vào `raw_cache/`.
5. **Trích bảng:** `extract_tables.py` → số liệu **PROVISIONAL**, phải người xác minh.
6. **Chuẩn hóa + ghi công:** `normalize.py` → CSV với đủ cột provenance, nhãn mặc định `Single-source/Provisional`.
7. **Nâng cấp confidence:** chỉ đặt `Corroborated` khi có nguồn độc lập thứ 2 (thường Tier-2 press).
8. **Cập nhật `CREDITS.md`** nếu thêm nguồn mới.

## Kỷ luật liêm chính
- Không suy diễn/ngoại suy/điền khoảng trống — gap thì ghi lại, không đoán.
- Extraction là nháp cho tới khi người kiểm; không tự tin số máy trích.
- Giữ nguyên attribution khi chia sẻ CSV; không gỡ ghi công.

## Phối hợp
- `data-analysis` (phân tích sau khi có CSV) · `citation-manager` (trích nguồn) · `aaouj-compliance` (nếu dữ liệu vào bài AAOUJ).

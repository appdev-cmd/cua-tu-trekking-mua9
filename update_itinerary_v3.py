# -*- coding: utf-8 -*-
import os
import re

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Tab 1 in Itinerary with the exact 1-day itinerary provided by the user
old_tab1_content = r'<div id="tab-day1" class="tab-content-panel"[\s\S]*?</div>\s*</div>\s*<!-- Tab 2:'

new_tab1_content = """<div id="tab-day1" class="tab-content-panel" style="background: white; border-radius: var(--radius-lg); padding: 32px; box-shadow: var(--shadow-sm); border: 1px solid var(--gray-200);">
        <div style="background: #e8f5ed; border-left: 4px solid var(--primary); padding: 14px 18px; border-radius: 8px; margin-bottom: 24px; font-size: 0.94rem; color: #064e3b; line-height: 1.55;">
          🟢 <strong>LỊCH TRÌNH 1 NGÀY:</strong> HÀ NỘI – HOÀNG NÔNG FARM – TREKKING SUỐI CỬA TỬ – HÀ NỘI <br/>
          <em>(Đi sáng về chiều, 16h00 về lại Farm tắm nước nóng, 16h30 lên xe về Hà Nội – Tối thứ 7 về đến nhà nghỉ ngơi thảnh thơi trọn vẹn Chủ Nhật!)</em>
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">05:30</div>
            <div class="timeline-title">Khởi hành từ Hà Nội lên Hoàng Nông Farm</div>
            <div class="timeline-desc">Quý khách tự túc phương tiện cá nhân hoặc xe chung di chuyển từ Hà Nội lên Hoàng Nông Farm (theo cao tốc Hà Nội - Thái Nguyên khoảng 2 tiếng).</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:00</div>
            <div class="timeline-title">Có mặt tại Hoàng Nông Farm</div>
            <div class="timeline-desc">Tập kết tại Farm, cất đồ đạc không cần thiết, nhận trang bị (áo phao trợ nổi, dép đi suối, túi chống nước 10L).</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:30</div>
            <div class="timeline-title">Xuất phát – Di chuyển bằng xe ôm đến chân núi</div>
            <div class="timeline-desc">Đội ngũ xe ôm bản địa chở từng thành viên vào chân núi, đảm bảo an toàn và thuận tiện.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:45</div>
            <div class="timeline-title">Đến cửa rừng – Nghe phổ biến lịch trình & an toàn</div>
            <div class="timeline-desc">Đến cửa rừng, nghe porter chuyên nghiệp phổ biến lịch trình chi tiết và các lưu ý an toàn bắt buộc khi vào suối.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">09:00</div>
            <div class="timeline-title">Bắt đầu trekking – Cửa đầu tiên Suối Cửa Tử</div>
            <div class="timeline-desc">Bắt đầu trekking, vượt qua đường mòn ven suối và cửa đầu tiên của Suối Cửa Tử trong làn nước nguồn mát lạnh, trong vắt.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">10:00</div>
            <div class="timeline-title">Check-in Cửa 2</div>
            <div class="timeline-desc">Khám phá hẻm suối kỳ vĩ, ngắm vách đá rêu phong và chụp ảnh lưu niệm cùng đồng đội.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">10:30</div>
            <div class="timeline-title">Check-in & Trải nghiệm nhảy thác rơi tự do</div>
            <div class="timeline-desc">Trải nghiệm nhảy thác cảm giác mạnh rơi tự do xuống hồ nước sâu <em>(tùy theo điều kiện thực tế và hướng dẫn của porter)</em>.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">11:30</div>
            <div class="timeline-title">Băng cánh rừng thứ hai – Trượt máng nước tự nhiên triệu năm</div>
            <div class="timeline-desc">Di chuyển qua cánh rừng thứ hai, bắt gặp máng trượt nước tự nhiên trơn láng triệu năm – một trong những điểm đặc sắc nhất của hành trình. <em>Quý khách tuyệt đối tuân thủ hướng dẫn của porter khi trượt thác.</em></div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">12:30</div>
            <div class="timeline-title">Dùng bữa trưa dã ngoại gần khu vực Thác Thiên Đường</div>
            <div class="timeline-desc">Nghỉ ngơi bên bờ đá rợp bóng cây, thưởng thức mâm cỗ 6 người thịnh soạn: Gà đồi nướng than hoa, ba chỉ quay giòn bì, xôi nếp nương tím thơm dẻo chấm muối vừng, hoa quả tráng miệng.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">14:00</div>
            <div class="timeline-title">Quay trở lại – Vượt qua hẻm suối Cửa Tử</div>
            <div class="timeline-desc">Bắt đầu quay trở lại, đi qua hẻm suối Cửa Tử kỳ vĩ, ngắm cảnh rừng đại ngàn hoang sơ. Xe ôm đón tại cửa rừng đưa về Farm.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">16:00</div>
            <div class="timeline-title">Về đến Hoàng Nông Farm – Tắm nóng lạnh, sấy tóc & Thưởng trà An Vân</div>
            <div class="timeline-desc">Quý khách tắm rửa, thay đồ, sử dụng khăn tắm, máy sấy tóc và đồ dùng tắm rửa tiện nghi đã được chuẩn bị sẵn. Dùng bữa ăn nhẹ, thưởng trà An Vân đặc sản và nghỉ ngơi tại không gian Farm.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">16:30</div>
            <div class="timeline-title">Lên xe trở về Hà Nội – Kết thúc tour 1 ngày</div>
            <div class="timeline-desc">Quý khách lên xe trở về Hà Nội (dự kiến về tới Hà Nội khoảng 18h30 - 19h00). Kết thúc chương trình trekking Suối Cửa Tử 1 ngày trọn vẹn và an toàn!</div>
          </div>
        </div>
      </div>

      <!-- Tab 2:"""

html = re.sub(old_tab1_content, new_tab1_content, html)

# 2. Add Organizers Note Banner in Safety Section
important_organizer_notice = """
      <!-- IMPORTANT ORGANIZER NOTICE BANNER -->
      <div style="background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: white; border-radius: var(--radius-lg); padding: 26px 28px; margin-bottom: 28px; box-shadow: 0 10px 30px rgba(30,27,75,0.25); border: 2px solid #818cf8;">
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
          <span style="font-size: 1.8rem; line-height: 1;">📢</span>
          <h3 style="font-size: 1.25rem; font-weight: 800; color: #fde047; text-transform: uppercase; letter-spacing: 0.5px; margin: 0;">
            LƯU Ý QUAN TRỌNG TỪ HOÀNG NÔNG FARM
          </h3>
        </div>
        <p style="font-size: 0.95rem; line-height: 1.6; color: #e0e7ff; margin-bottom: 12px;">
          🌿 <strong>ĐÂY LÀ TRẢI NGHIỆM THIÊN NHIÊN, KHÔNG PHẢI TOUR NGHỈ DƯỠNG THÔNG THƯỜNG:</strong> Quý khách vui lòng chuẩn bị tinh thần vận động thể lực và tuân thủ tuyệt đối mọi hướng dẫn của ban tổ chức và đội ngũ porter!
        </p>
        <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px; font-size: 0.92rem; color: #c7d2fe;">
          <li style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="color: #fde047; font-weight: bold;">•</span>
            <div><strong>An toàn là số 1:</strong> Hoàng Nông Farm luôn đặt an toàn của khách hàng lên hàng đầu trong mọi tình huống.</div>
          </li>
          <li style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="color: #fde047; font-weight: bold;">•</span>
            <div><strong>Linh hoạt theo thời tiết & thể lực:</strong> Lịch trình thực tế có thể thay đổi tùy theo điều kiện thời tiết, thể lực thực tế của đoàn và đánh giá an toàn của porter.</div>
          </li>
          <li style="display: flex; align-items: flex-start; gap: 8px;">
            <span style="color: #fde047; font-weight: bold;">•</span>
            <div><strong>Điều kiện hoãn:</strong> Chương trình có thể tạm hoãn hoặc điều chỉnh nếu thời tiết xấu, mưa lớn, nước suối dâng cao hoặc điều kiện không đảm bảo an toàn.</div>
          </li>
        </ul>
      </div>
"""

# Inject this notice before the 11 safety rules in safety-section
target_safety_marker = '<div style="background: white; border-radius: var(--radius-lg); padding: 30px;'
if target_safety_marker in html:
    html = html.replace(target_safety_marker, important_organizer_notice + '\n      ' + target_safety_marker, 1)

# 3. Add explicit rules in the 11 safety rules:
# "Không tự ý xuống nước, bơi hoặc trượt thác khi chưa có hướng dẫn"
old_porter_rule = """          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #e8f5ed; border-radius: 10px; border-left: 3px solid #10b981;">
            <span style="font-size: 1.25rem;">🦺</span>
            <div style="font-size: 0.92rem;"><strong>Tuân thủ lệnh porter:</strong> Tuân thủ đầy đủ hướng dẫn của porter trong toàn bộ hành trình khi trượt thác hoặc nhảy thác.</div>
          </div>"""

new_porter_rule = """          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #e8f5ed; border-radius: 10px; border-left: 3px solid #10b981;">
            <span style="font-size: 1.25rem;">🦺</span>
            <div style="font-size: 0.92rem;"><strong>Tuân thủ lệnh porter:</strong> Tuân thủ đầy đủ hướng dẫn của porter trong toàn bộ hành trình. <strong>Không tự ý xuống nước, bơi hoặc trượt thác khi chưa có hướng dẫn!</strong></div>
          </div>"""

html = html.replace(old_porter_rule, new_porter_rule)

# 4. Update Option 1 card subtitle & details to reflect 16h30 return time
old_opt1_sub = '<p class="option-subtitle">Khởi hành: <strong>Thứ Bảy, 10/10/2026</strong> (05:30 – 19:00)</p>'
new_opt1_sub = '<p class="option-subtitle">Khởi hành: <strong>Thứ Bảy, 10/10/2026</strong> (05:30 – 16h30 lên xe về)</p>'
html = html.replace(old_opt1_sub, new_opt1_sub)

old_opt1_perk = '<div><strong>Lịch trình gọn gàng:</strong> Đi sáng sớm từ Hà Nội, chiều tối về lại nhà, Chủ Nhật nghỉ ngơi thong thả cùng gia đình.</div>'
new_opt1_perk = '<div><strong>Lịch trình siêu gọn:</strong> 5h30 xuất phát Hà Nội ➔ 16h00 về Farm tắm nóng lạnh, thưởng trà ➔ 16h30 lên xe về Hà Nội (18h30-19h00 về tới nhà), Chủ Nhật thảnh thơi cùng gia đình.</div>'
html = html.replace(old_opt1_perk, new_opt1_perk)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(base_dir, "template.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html and template.html with exact 1-day itinerary & organizer notice!")

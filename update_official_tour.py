# -*- coding: utf-8 -*-
import os
import re

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero meta tag with Google Maps link
old_loc_meta = """            <div class="meta-tag">
              <span>📍</span>
              <span>Địa điểm: <strong>Suối Cửa Tử – Thái Nguyên</strong></span>
            </div>"""

new_loc_meta = """            <div class="meta-tag">
              <span>📍</span>
              <span>Địa điểm: <strong>Hoàng Nông Farm – Suối Cửa Tử (Thái Nguyên)</strong></span>
              <a href="https://maps.app.goo.gl/wbJSxNpZYTU7Q5uDA?g_st=ipc" target="_blank" style="margin-left: 8px; font-size: 0.8rem; background: #f59e0b; color: #000; font-weight: 800; padding: 2px 8px; border-radius: 6px; text-decoration: none;">🗺️ Mở Maps</a>
            </div>"""

html = html.replace(old_loc_meta, new_loc_meta)

# 2. Add Cung Trekking 10km Overview Banner right before or inside Itinerary Section
trail_overview_html = """
  <!-- TREKKING ROUTE OVERVIEW -->
  <div style="background: linear-gradient(135deg, #062b1e 0%, #0d5c3e 100%); color: white; border-radius: var(--radius-lg); padding: 28px 24px; margin-bottom: 30px; box-shadow: 0 10px 30px rgba(6,43,30,0.3); border: 1px solid rgba(255,255,255,0.15);">
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 20px;">
      <div>
        <span style="background: rgba(245,158,11,0.25); color: #fde047; font-weight: 800; font-size: 0.78rem; padding: 4px 12px; border-radius: 999px; border: 1px solid rgba(245,158,11,0.5);">CUNG ĐƯỜNG TREKKING HOÀNG NÔNG FARM</span>
        <h3 style="font-size: 1.45rem; font-weight: 800; margin-top: 6px; color: #ffffff;">Chinh Phục 10 Cửa Suối Cửa Tử (Tổng ~10km Khứ Hồi)</h3>
      </div>
      <a href="https://maps.app.goo.gl/wbJSxNpZYTU7Q5uDA?g_st=ipc" target="_blank" style="background: #f59e0b; color: #000; font-weight: 800; padding: 10px 18px; border-radius: 999px; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 15px rgba(245,158,11,0.4); font-size: 0.92rem;">
        <span>📍 Định vị Google Maps Farm</span>
        <span>↗</span>
      </a>
    </div>

    <!-- Route Steps Pills -->
    <div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center; margin-bottom: 18px; font-size: 0.88rem; font-weight: 700;">
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">🏡 Hoàng Nông Farm</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">🚪 Hẻm Cửa 1</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">🚪 Cửa 2</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">🌊 Thác Nhảy Rơi Tự Do</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">⚡ Thác Trượt Máng Đá</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">✨ Thác Thiên Đường</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(255,255,255,0.15); padding: 6px 12px; border-radius: 8px;">🏞️ Cửa 5-6-7-8-9-10</span>
      <span style="color: #fde047;">➔</span>
      <span style="background: rgba(245,158,11,0.25); color: #fde047; padding: 6px 12px; border-radius: 8px; border: 1px solid #f59e0b;">Quay về Farm (18h00)</span>
    </div>

    <p style="font-size: 0.92rem; color: #d1fae5; line-height: 1.6; margin: 0;">
      🌲 <strong>Địa hình đa dạng:</strong> Sườn núi, đường rừng nguyên sinh, suối đá, hẻm suối, dốc núi, thác nước. Trong hành trình, bạn sẽ trải nghiệm trượt máng đá tự nhiên triệu năm, bơi dưới chân thác, tắm suối mát lạnh, đi qua cầu gỗ, bơi hoặc đi thuyền vượt hẻm suối. <em>(Hoạt động nhảy thác rơi tự do chỉ được thực hiện khi điều kiện nước an toàn và có lệnh của porter)</em>.
    </p>
  </div>
"""

# 3. Update Itinerary Timelines with the exact Official Schedule
new_itinerary_content = """  <!-- ITINERARY DETAILS -->
  <section class="section" id="itinerary-section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">KẾ HOẠCH HÀNH TRÌNH CHÍNH THỨC</span>
        <h2 class="section-title">Lịch Trình Chi Tiết Trekking Suối Cửa Tử</h2>
        <p class="section-desc">Hoàng Nông Farm tổ chức điều phối và dẫn đoàn đảm bảo an toàn tuyệt đối</p>
      </div>

""" + trail_overview_html + """

      <div class="tabs-nav">
        <button class="tab-btn active" onclick="switchItineraryTab('tab-day1', this)">Phương Án 1: Đi Trong Ngày (Thứ 7 ngày 10/10)</button>
        <button class="tab-btn" onclick="switchItineraryTab('tab-day2', this)">Phương Án 2: Đi 2 Ngày 1 Đêm (10 – 11/10/2026)</button>
      </div>

      <!-- Tab 1: Đi trong ngày -->
      <div id="tab-day1" class="tab-content-panel" style="background: white; border-radius: var(--radius-lg); padding: 32px; box-shadow: var(--shadow-sm); border: 1px solid var(--gray-200);">
        <div style="background: #e8f5ed; border-left: 4px solid var(--primary); padding: 12px 18px; border-radius: 8px; margin-bottom: 24px; font-size: 0.94rem; color: #064e3b;">
          🟢 <strong>ĐẶC ĐIỂM PA 1:</strong> Khởi hành sáng sớm từ Hà Nội, trekking trọn vẹn cung suối cùng đoàn, tắm rửa nóng lạnh sạch sẽ tại Farm rồi lên xe về lại Hà Nội vào tối Thứ 7. Chủ nhật thong thả nghỉ ngơi tại nhà!
        </div>

        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">05:30</div>
            <div class="timeline-title">Khởi hành từ Hà Nội đi Hoàng Nông Farm</div>
            <div class="timeline-desc">Đoàn tập kết / tự túc phương tiện cá nhân hoặc xe chung di chuyển theo cao tốc Hà Nội - Thái Nguyên (khoảng 2 tiếng).</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:00</div>
            <div class="timeline-title">Có mặt tại Hoàng Nông Farm – Tập kết & Nhận trang bị</div>
            <div class="timeline-desc">Tập kết tại Farm, cất đồ đạc không cần thiết, nhận áo phao trợ nổi, dép đi suối, túi khô chống nước 10L và nghe porter phổ biến an toàn.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:30 – 08:45</div>
            <div class="timeline-title">Xe ôm chở vào chân núi – Đến cửa rừng</div>
            <div class="timeline-desc">Xe ôm địa phương trung chuyển đoàn từ Farm vào tận chân núi, tập hợp tại cửa rừng chuẩn bị vào suối.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">09:00</div>
            <div class="timeline-title">Bắt đầu trekking – Chinh phục Cửa 1 Suối Cửa Tử</div>
            <div class="timeline-desc">Vượt qua đường mòn ven suối rợp bóng mát, lội qua làn nước trong vắt và cửa đầu tiên của Suối Cửa Tử.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">10:00</div>
            <div class="timeline-title">Check-in Cửa 2</div>
            <div class="timeline-desc">Chiêm ngưỡng vách đá kỳ vĩ và dòng suối nguồn xanh biếc uốn lượn giữa đại ngàn Đông Tam Đảo.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">10:30</div>
            <div class="timeline-title">Trải nghiệm Thác Nhảy (Nhảy thác rơi tự do)</div>
            <div class="timeline-desc">Thử thách cảm giác mạnh nhảy thác rơi tự do xuống hồ nước sâu <em>(chỉ thực hiện khi điều kiện nước an toàn và có porter hướng dẫn kèm sát)</em>.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">11:30</div>
            <div class="timeline-title">Băng cánh rừng thứ hai – Máng trượt nước tự nhiên triệu năm</div>
            <div class="timeline-desc">Trải nghiệm máng trượt nước tự nhiên trơn láng do dòng nước bào mòn hàng triệu năm – một trong những điểm đặc sắc nhất hành trình!</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">12:00</div>
            <div class="timeline-title">Ăn trưa dã ngoại thịnh soạn bên suối (Khu vực Cửa 6 hoặc Cửa 7)</div>
            <div class="timeline-desc">Mâm cỗ 6 người thịnh soạn bày trên lá dong bên bờ đá: Gà đồi nướng than hoa, ba chỉ quay giòn bì, xôi nếp nương tím thơm dẻo, hoa quả tráng miệng.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">13:00 – 15:00</div>
            <div class="timeline-title">Trekking liên tục từ Cửa 7 đến Cửa 10 – Thác Thiên Đường</div>
            <div class="timeline-desc">Đoàn khám phá cung suối hoang sơ sâu nhất, chiêm ngưỡng thác Thiên Đường và các hồ nước ngọc bích trong veo.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">15:30</div>
            <div class="timeline-title">Quay trở lại – Bơi hoặc đi thuyền vượt hẻm Cửa Tử</div>
            <div class="timeline-desc">Thong thả di chuyển ngược lại đường cũ, vượt qua hẻm suối Cửa Tử kỳ vĩ, ra đến cửa rừng có xe ôm đón về Farm.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">18:00</div>
            <div class="timeline-title">Về đến Hoàng Nông Farm – Tắm nóng lạnh & Thay đồ</div>
            <div class="timeline-desc">Tắm rửa nước nóng thoải mái tại khu phòng tắm tiện nghi của Farm, sấy tóc, thưởng trà An Vân và bánh nhẹ.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">18:45 – 20:45</div>
            <div class="timeline-title">Lên xe trở về Hà Nội – Kết thúc tour 1 ngày trọn vẹn</div>
            <div class="timeline-desc">Xe đưa đoàn về lại Hà Nội vào buổi tối, sẵn sàng cho ngày Chủ Nhật thảnh thơi bên gia đình.</div>
          </div>
        </div>
      </div>

      <!-- Tab 2: Đi 2 ngày 1 đêm -->
      <div id="tab-day2" class="tab-content-panel" style="display: none; background: white; border-radius: var(--radius-lg); padding: 32px; box-shadow: var(--shadow-sm); border: 1px solid var(--gray-200);">
        <div style="background: #fef3c7; border-left: 4px solid var(--amber-dark); padding: 12px 18px; border-radius: 8px; margin-bottom: 24px; font-size: 0.94rem; color: #92400e;">
          🟠 <strong>ĐẶC ĐIỂM PA 2:</strong> Toàn bộ lịch trình trekking Ngày 1 giống hệt PA 1, nhưng ở lại Hoàng Nông Farm để tham dự <strong>Đại Tiệc Gala Tổng Kết Mùa 9</strong>, vinh danh trao thưởng, giao lưu lửa trại, ngủ đêm phòng tiện nghi và sáng hôm sau chạy trail đồi chè La Bằng!
        </div>

        <h4 style="color: var(--amber-dark); font-weight: 800; margin-bottom: 16px; font-size: 1.15rem;">
          🌟 NGÀY 1 (THỨ BẢY 10/10): HÀ NỘI – HOÀNG NÔNG FARM – CHINH PHỤC 10 CỬA – GALA TỔNG KẾT MÙA 9
        </h4>
        <div class="timeline" style="margin-bottom: 30px;">
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">05:30 – 08:00</div>
            <div class="timeline-title">Di chuyển Hà Nội – Hoàng Nông Farm</div>
            <div class="timeline-desc">Có mặt tại Farm lúc 8h00, nhận áo phao, dép rọ, túi chống nước và gửi hành lý tại phòng nghỉ.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">08:30 – 12:00</div>
            <div class="timeline-title">Trekking Cửa 1, Cửa 2, Nhảy Thác & Máng trượt nước tự nhiên</div>
            <div class="timeline-desc">Xe ôm vào cửa rừng (8h45), bắt đầu trek (9h00), check-in Cửa 2 (10h00), trải nghiệm thác nhảy (10h30), trượt máng đá triệu năm (11h30).</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">12:00 – 15:30</div>
            <div class="timeline-title">Ăn trưa dã ngoại mâm gà đồi (Cửa 6/7) – Trekking sâu Cửa 10</div>
            <div class="timeline-desc">Thưởng thức mâm cỗ dã ngoại bờ suối, từ 13h00-15h00 tiếp tục trek sâu khám phá đến tận Cửa 10 hoang sơ kỳ vĩ.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">15:30 – 18:00</div>
            <div class="timeline-title">Vượt hẻm suối Cửa Tử – Về lại Hoàng Nông Farm</div>
            <div class="timeline-desc">Quay về theo đường cũ, bơi/đi thuyền qua hẻm suối, xe ôm đón về Farm lúc 18h00. Tắm nóng lạnh sảng khoái, thay đồ.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">19:00 – 22:00</div>
            <div class="timeline-title">Đại tiệc BBQ & GALA BẾ MẠC TỔNG KẾT MÙA 9</div>
            <div class="timeline-desc">Dùng bữa tối thịnh soạn tại Farm. Vinh danh các chiến binh 100 ngày kiên trì bơi lội & chạy bộ, trao thưởng chiến thần, chia quỹ và nâng ly giao lưu tưng bừng!</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot" style="background: var(--amber-dark); box-shadow: 0 0 0 2px var(--amber-dark);"></div>
            <div class="timeline-time">22:00</div>
            <div class="timeline-title">Nghỉ ngơi tại Hoàng Nông Farm</div>
            <div class="timeline-desc">Giữ yên tĩnh cho không gian chung, ngủ đêm trong phòng nghỉ điều hòa tiện nghi view núi rừng.</div>
          </div>
        </div>

        <h4 style="color: var(--primary); font-weight: 800; margin-bottom: 16px; font-size: 1.15rem;">
          🍃 NGÀY 2 (CHỦ NHẬT 11/10): CHẠY TRAIL ĐỒI CHÈ LA BẰNG – THƯỞNG TRÀ AN VÂN – HÀ NỘI
        </h4>
        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">05:00 – 07:30</div>
            <div class="timeline-title">Chạy trail trên đồi chè La Bằng (Tự nguyện cho các Runner)</div>
            <div class="timeline-desc">Đón bình minh trong trẻo trên đồi chè La Bằng bát ngát ngút ngàn, tận hưởng không khí trong lành miền sơn cước.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">08:00 – 09:00</div>
            <div class="timeline-title">Dùng bữa sáng tại Hoàng Nông Farm</div>
            <div class="timeline-desc">Thưởng thức bữa sáng nạp năng lượng tươi mới ngắm mây núi Tam Đảo.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">09:00 – 11:30</div>
            <div class="timeline-title">Không gian thưởng trà An Vân – Thư giãn & Chụp ảnh</div>
            <div class="timeline-desc">Thưởng thức tách trà An Vân đặc sản trứ danh tại không gian trà đạo của Farm, thư thả chụp ảnh check-in sống ảo.</div>
          </div>
          <div class="timeline-item">
            <div class="timeline-dot"></div>
            <div class="timeline-time">12:00</div>
            <div class="timeline-title">Check-out Farm – Lên xe trở về Hà Nội</div>
            <div class="timeline-desc">Đoàn trả phòng, lên xe trở về Hà Nội. Kết thúc chuyến offline bế mạc Mùa 9 đầy ắp kỷ niệm đáng nhớ!</div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Replace existing itinerary section
pattern_itinerary = r'  <!-- ITINERARY DETAILS -->[\s\S]*?</section>'
html = re.sub(pattern_itinerary, new_itinerary_content, html)

# 4. Update the Packing Checklist Section with the exact items (Nam, Nữ, Giày, Đồ cá nhân, Đồ cấm)
new_packing_html = """  <!-- PACKING & GEAR CHECKLIST SECTION -->
  <section class="section" id="packing-section" style="background: var(--gray-100);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #e0e7ff; color: #3730a3;">🎒 HÀNH TRANG THAM GIA</span>
        <h2 class="section-title">Quý Khách Cần Chuẩn Bị Những Gì?</h2>
        <p class="section-desc">
          Để chuyến đi trọn vẹn, an toàn và có những bức ảnh sống ảo đẹp nhất, mọi người chuẩn bị hành trang theo hướng dẫn chi tiết từ Hoàng Nông Farm:
        </p>
      </div>

      <div class="packing-grid">
        <!-- Card 1: BTC đã chuẩn bị -->
        <div class="packing-card included">
          <div class="packing-header">
            <div class="packing-icon">🦺</div>
            <div class="packing-title-box">
              <h3>Farm & Tour Đã Có Sẵn</h3>
              <span class="packing-badge badge-green">✓ Không cần tự mang</span>
            </div>
          </div>
          <ul class="checklist-list">
            <li>
              <span class="c-icon">🦺</span>
              <div><strong>Áo phao trợ nổi đạt chuẩn:</strong> Có đủ size cho mọi người, trợ nổi 100% kể cả người không biết bơi.</div>
            </li>
            <li>
              <span class="c-icon">👟</span>
              <div><strong>Dép tổ ong đi suối:</strong> Farm đã chuẩn bị sẵn dép tổ ong chuyên dụng lội suối cho quý khách.</div>
            </li>
            <li>
              <span class="c-icon">🎒</span>
              <div><strong>Túi khô chống nước 10L:</strong> Để đựng điện thoại, đồ ăn nhẹ mang vào suối.</div>
            </li>
            <li>
              <span class="c-icon">🦯</span>
              <div><strong>Gậy trekking:</strong> Hỗ trợ trợ lực cho các đoạn đi dốc rừng gập ghềnh.</div>
            </li>
            <li>
              <span class="c-icon">🍗</span>
              <div><strong>Mâm cỗ gà đồi nướng:</strong> Bữa trưa dã ngoại bờ suối + nước uống đóng chai suốt tuyến.</div>
            </li>
            <li>
              <span class="c-icon">🚿</span>
              <div><strong>Phòng tắm nóng lạnh Farm:</strong> Có sẵn máy sấy tóc, dầu gội, sữa tắm khi kết thúc trek.</div>
            </li>
          </ul>
        </div>

        <!-- Card 2: Đồ cá nhân cần chuẩn bị (Nam & Nữ) -->
        <div class="packing-card bring">
          <div class="packing-header">
            <div class="packing-icon">🎒</div>
            <div class="packing-title-box">
              <h3>Đồ Cá Nhân Cần Chuẩn Bị</h3>
              <span class="packing-badge badge-blue">★ Bắt buộc / Nên mang</span>
            </div>
          </div>
          <ul class="checklist-list">
            <li>
              <span class="c-icon">🪪</span>
              <div><strong>Giấy tờ tùy thân:</strong> CCCD / CMND / Hộ chiếu khớp với thông tin đăng ký.</div>
            </li>
            <li>
              <span class="c-icon">👟</span>
              <div><strong>Giày đi suối khuyên dùng:</strong> Giày leo núi thoát nước nhanh hoặc giày chạy trail nhẹ, nhanh khô (bên cạnh dép tổ ong Farm).</div>
            </li>
            <li>
              <span class="c-icon">🩳</span>
              <div><strong>Trang phục Nam:</strong> Đồ bơi, quần short dễ vận động, chất liệu nhanh khô.</div>
            </li>
            <li>
              <span class="c-icon">🩱</span>
              <div><strong>Trang phục Nữ:</strong> Đồ bơi, áo bra, bikini, quần áo dễ vận động mau khô, áo khoác dài mỏng mặc ngoài nếu cần.</div>
            </li>
            <li>
              <span class="c-icon">🧤</span>
              <div><strong>Bảo hộ:</strong> Găng tay, tất cao cổ (chống vắt/cào xước), mũ phù hợp khi đi rừng.</div>
            </li>
            <li>
              <span class="c-icon">🥽</span>
              <div><strong>Bơi lội:</strong> Kính bơi, bao chống nước cho điện thoại có dây đeo cổ.</div>
            </li>
            <li>
              <span class="c-icon">💧</span>
              <div><strong>Năng lượng & Nước:</strong> Bình nước cá nhân, kẹo ngọt, Snickers, kẹo gừng, socola, viên C sủi, nước điện giải.</div>
            </li>
            <li>
              <span class="c-icon">🧴</span>
              <div><strong>Vệ sinh & Da:</strong> Kem chống nắng, thuốc xịt côn trùng, bàn chải đánh răng (đặc biệt cho ai ngủ đêm PA 2).</div>
            </li>
          </ul>
        </div>

        <!-- Card 3: Những thứ không nên mang -->
        <div class="packing-card avoid">
          <div class="packing-header">
            <div class="packing-icon">🚫</div>
            <div class="packing-title-box">
              <h3>Những Thứ KHÔNG Nên Mang</h3>
              <span class="packing-badge badge-red">⚠️ Lưu ý tránh</span>
            </div>
          </div>
          <ul class="checklist-list">
            <li>
              <span class="c-icon">❌</span>
              <div><strong>KHÔNG mang giày leo núi chống nước (Gore-Tex), giày đế cứng:</strong> Nước suối tràn vào sẽ đọng kín bên trong, nặng như chì.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>KHÔNG mặc váy, áo dài, đồ jean:</strong> Trang phục cầu kỳ ngấm nước rất nặng, cản trở di chuyển và gây rát da.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>KHÔNG đeo trang sức quý giá, nhẫn vàng:</strong> Dòng nước chảy xiết và leo trèo rất dễ làm tuột rơi xuống đáy suối sâu.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>KHÔNG đi dép lê, dép lào xỏ ngón:</strong> Trơn trượt nguy hiểm trên đá rêu phong và bị dòng nước cuốn trôi.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>KHÔNG mang ví tiền dày & giấy tờ không cần thiết:</strong> Chỉ cần CCCD và ít tiền mặt, đồ đạc có giá trị nên gửi tại lễ tân Farm.</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>
"""

pattern_packing = r'  <!-- PACKING & GEAR CHECKLIST SECTION -->[\s\S]*?</section>'
html = re.sub(pattern_packing, new_packing_html, html)

# 5. Update Health & Safety Rules section with all 11 official rules from organizer
new_safety_html = """  <!-- FAQS & PACKING LIST -->
  <section class="section" id="safety-section">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #fee2e2; color: #991b1b;">🛡️ AN TOÀN LÀ TRÊN HẾT</span>
        <h2 class="section-title">Lưu Ý Về Sức Khỏe & Quy Tắc An Toàn Bắt Buộc</h2>
        <p class="section-desc">Để đảm bảo an toàn tuyệt đối cho bản thân và toàn đoàn, quý khách vui lòng đọc kỹ và tuân thủ các quy tắc sau:</p>
      </div>

      <!-- 11 Safety & Health Rules Card -->
      <div style="background: white; border-radius: var(--radius-lg); padding: 30px; box-shadow: var(--shadow-sm); border: 1px solid var(--gray-200); margin-bottom: 30px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: var(--gray-50); border-radius: 10px; border-left: 3px solid #10b981;">
            <span style="font-size: 1.25rem;">🏃‍♂️</span>
            <div style="font-size: 0.92rem;"><strong>Tập thể lực trước chuyến đi:</strong> Quý khách nên tập thể lực trước chuyến đi khoảng 1 tuần <em>(chiến binh 100 ngày đã hoàn toàn sẵn sàng!)</em>.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #fff1f2; border-radius: 10px; border-left: 3px solid #f43f5e;">
            <span style="font-size: 1.25rem;">❤️</span>
            <div style="font-size: 0.92rem;"><strong>Tiền sử bệnh lý:</strong> <strong>KHÔNG</strong> tham gia nếu có tiền sử bệnh tim mạch, huyết áp hoặc các vấn đề sức khỏe không phù hợp với vận động cường độ cao.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #fff1f2; border-radius: 10px; border-left: 3px solid #f43f5e;">
            <span style="font-size: 1.25rem;">🤰</span>
            <div style="font-size: 0.92rem;"><strong>Phụ nữ mang thai:</strong> Phụ nữ đang mang thai <strong>tuyệt đối không</strong> tham gia hành trình trekking suối.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: var(--gray-50); border-radius: 10px; border-left: 3px solid #f59e0b;">
            <span style="font-size: 1.25rem;">💅</span>
            <div style="font-size: 0.92rem;"><strong>Cắt ngắn móng tay, móng chân:</strong> Bắt buộc cắt ngắn trước khi tham gia để tránh dập móng hoặc chấn thương khi lội suối đá.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #fff1f2; border-radius: 10px; border-left: 3px solid #f43f5e;">
            <span style="font-size: 1.25rem;">👥</span>
            <div style="font-size: 0.92rem;"><strong>Không tự ý tách đoàn:</strong> Tuyệt đối không tự ý tách đoàn hoặc rẽ nhánh riêng khi di chuyển trong rừng già.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #fff1f2; border-radius: 10px; border-left: 3px solid #f43f5e;">
            <span style="font-size: 1.25rem;">🚶‍♂️</span>
            <div style="font-size: 0.92rem;"><strong>Không vượt trước porter:</strong> Porter là người bản địa am hiểu luồng lạch, hang đá ngầm và dòng nước sâu. Luôn đi sau porter dẫn đầu.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #e8f5ed; border-radius: 10px; border-left: 3px solid #10b981;">
            <span style="font-size: 1.25rem;">🦺</span>
            <div style="font-size: 0.92rem;"><strong>Tuân thủ lệnh porter:</strong> Tuân thủ đầy đủ hướng dẫn của porter trong toàn bộ hành trình khi trượt thác hoặc nhảy thác.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: var(--gray-50); border-radius: 10px; border-left: 3px solid #3b82f6;">
            <span style="font-size: 1.25rem;">🌧️</span>
            <div style="font-size: 0.92rem;"><strong>Điều kiện thời tiết:</strong> Chương trình có thể hoãn hoặc điều chỉnh do thời tiết xấu, mưa lũ hoặc điều kiện suối không đảm bảo an toàn.</div>
          </div>

          <div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; background: #e8f5ed; border-radius: 10px; border-left: 3px solid #10b981; grid-column: span 2;">
            <span style="font-size: 1.25rem;">🌿</span>
            <div style="font-size: 0.92rem;"><strong>Bảo vệ thiên nhiên:</strong> <strong>TUYỆT ĐỐI KHÔNG XẢ RÁC</strong> ra môi trường. Mọi vỏ bánh, chai lọ đều gom vào túi khô mang về Farm xử lý.</div>
          </div>
        </div>
      </div>

      <div class="features-grid">
        <div class="feature-card">
          <h3 style="color: var(--amber-dark);">🤝 Không tham gia Mùa 9 có được đi không?</h3>
          <p>
            <strong>Cực kỳ hoan nghênh và welcome 100%!</strong> Chuyến đi mở rộng cho tất cả anh chị em, bạn bè, người thân, đồng nghiệp. <strong>Kinh phí chuyến đi được chia đều công bằng cho tất cả những ai tham gia trekking</strong>, không phân biệt thành viên Mùa 9 hay khách mời!
          </p>
        </div>

        <div class="feature-card">
          <h3 style="color: #e11d48;">🚨 Đã vote tham gia rồi có được đổi ý / hủy không?</h3>
          <p>
            <strong>Tuyệt đối KHÔNG được thay đổi quyết định!</strong> Tour suối Cửa Tử tính chi phí theo nguyên tắc chia đều cho những người tham gia, đồng thời Ban tổ chức phải đặt cọc trước phòng Farm, xe ôm trung chuyển, mâm cơm suối và ký hợp đồng với porter dẫn đường. Việc một người đổi ý hủy kèo sẽ làm đội chi phí của tất cả những người còn lại và làm đảo lộn kế hoạch của cả đoàn!
          </p>
        </div>

        <div class="feature-card">
          <h3 style="color: var(--primary);">🏊 Không biết bơi có đi được không?</h3>
          <p>
            <strong>Chắc chắn 100% đi được!</strong> Ban tổ chức trang bị áo phao cứu sinh trợ nổi chất lượng cao. Bạn chỉ cần mặc áo phao là nổi bồng bềnh 100%, hơn nữa luôn có các anh porter bản địa dày kinh nghiệm đi kèm hỗ trợ từng bước chân.
          </p>
          <div style="margin-top: 10px; display: flex; align-items: center; gap: 10px; background: var(--gray-50); padding: 8px; border-radius: 8px; cursor: pointer; border: 1px solid var(--gray-200);" onclick="openLightbox('images/cua-tu-porter-dong-hanh-loi-suoi.jpg', 'Hình ảnh thực tế: Đội ngũ porter mang vác áo phao trợ nổi đồng hành sát sườn cùng đoàn lội suối')">
            <img src="images/cua-tu-porter-dong-hanh-loi-suoi.jpg" alt="Porter đồng hành an toàn" style="width: 60px; height: 45px; object-fit: cover; border-radius: 6px;" />
            <span style="font-size: 0.82rem; font-weight: 700; color: var(--primary);">📸 Xem hình ảnh thực tế: Porter kèm áo phao trợ nổi sát sườn đoàn ↗</span>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

pattern_safety = r'  <!-- FAQS & PACKING LIST -->[\s\S]*?</section>'
html = re.sub(pattern_safety, new_safety_html, html)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(base_dir, "template.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html and template.html with official tour itinerary & safety rules!")

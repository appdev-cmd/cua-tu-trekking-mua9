# -*- coding: utf-8 -*-
import os

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

packing_css = """
    /* Packing Checklist Section */
    .packing-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      margin-top: 15px;
    }
    @media (max-width: 900px) {
      .packing-grid {
        grid-template-columns: 1fr;
      }
    }
    .packing-card {
      background: white;
      border-radius: var(--radius-md);
      padding: 26px 24px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--gray-200);
      display: flex;
      flex-direction: column;
      position: relative;
    }
    .packing-card.included {
      border-top: 4px solid #10b981;
    }
    .packing-card.bring {
      border-top: 4px solid #3b82f6;
    }
    .packing-card.avoid {
      border-top: 4px solid #f43f5e;
    }
    .packing-header {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 18px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--gray-200);
    }
    .packing-icon {
      font-size: 2rem;
      line-height: 1;
    }
    .packing-title-box h3 {
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 2px;
    }
    .packing-badge {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 800;
      padding: 2px 8px;
      border-radius: var(--radius-full);
      text-transform: uppercase;
    }
    .badge-green { background: #dcfce7; color: #15803d; }
    .badge-blue { background: #dbeafe; color: #1d4ed8; }
    .badge-red { background: #ffe4e6; color: #be123c; }

    .checklist-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 12px;
      font-size: 0.92rem;
      color: var(--gray-800);
      line-height: 1.5;
    }
    .checklist-list li {
      display: flex;
      align-items: flex-start;
      gap: 10px;
    }
    .checklist-list .c-icon {
      font-size: 1.1rem;
      flex-shrink: 0;
      margin-top: 1px;
    }
"""

packing_html = """  <!-- PACKING & GEAR CHECKLIST SECTION -->
  <section class="section" id="packing-section" style="background: var(--gray-100);">
    <div class="container">
      <div class="section-header">
        <span class="section-tag" style="background: #e0e7ff; color: #3730a3;">🎒 HÀNH TRANG THAM GIA</span>
        <h2 class="section-title">Gợi Ý Chuẩn Bị Đồ Đi Suối Cửa Tử</h2>
        <p class="section-desc">
          Để chuyến đi an toàn, thoải mái và có những bức ảnh sống ảo đẹp nhất, mọi người tham khảo checklist chuẩn bị bên dưới nhé!
        </p>
      </div>

      <div class="packing-grid">
        <!-- Card 1: BTC đã có sẵn -->
        <div class="packing-card included">
          <div class="packing-header">
            <div class="packing-icon">🦺</div>
            <div class="packing-title-box">
              <h3>BTC & Tour Đã Có Sẵn</h3>
              <span class="packing-badge badge-green">✓ Không cần tự mang</span>
            </div>
          </div>
          <ul class="checklist-list">
            <li>
              <span class="c-icon">🦺</span>
              <div><strong>Áo phao trợ nổi đạt chuẩn:</strong> Có đủ size, trợ nổi 100% kể cả người không biết bơi.</div>
            </li>
            <li>
              <span class="c-icon">👟</span>
              <div><strong>Dép rọ chuyên dụng lội suối:</strong> Đế bám đá chống trơn, thoát nước siêu nhanh.</div>
            </li>
            <li>
              <span class="c-icon">🎒</span>
              <div><strong>Túi khô chống nước 10L:</strong> Để đựng điện thoại, đồ ăn nhẹ mang vào suối.</div>
            </li>
            <li>
              <span class="c-icon">🦯</span>
              <div><strong>Gậy trekking:</strong> Hỗ trợ trợ lực cho các đoạn đi dốc trong rừng.</div>
            </li>
            <li>
              <span class="c-icon">🍗</span>
              <div><strong>Mâm cỗ ăn trưa bên suối:</strong> Bữa chính thịnh soạn + nước suối đóng chai.</div>
            </li>
            <li>
              <span class="c-icon">🚿</span>
              <div><strong>Phòng tắm nóng lạnh Farm:</strong> Có sẵn máy sấy tóc, dầu gội, sữa tắm khi về.</div>
            </li>
          </ul>
        </div>

        <!-- Card 2: Đồ cá nhân cần mang -->
        <div class="packing-card bring">
          <div class="packing-header">
            <div class="packing-icon">🎒</div>
            <div class="packing-title-box">
              <h3>Đồ Cá Nhân Cần Chuẩn Bị</h3>
              <span class="packing-badge badge-blue">★ Tự mang theo</span>
            </div>
          </div>
          <ul class="checklist-list">
            <li>
              <span class="c-icon">👕</span>
              <div><strong>Trang phục lội suối mau khô:</strong> Áo thun thể thao + quần dù/short nhanh ráo (hoặc legging dài chống xước cành cây).</div>
            </li>
            <li>
              <span class="c-icon">🧺</span>
              <div><strong>01 - 02 bộ quần áo khô sạch:</strong> Để trong balo gửi lại Farm thay sau khi đi suối về (kèm đồ lót dự phòng).</div>
            </li>
            <li>
              <span class="c-icon">📱</span>
              <div><strong>Bao chống nước điện thoại:</strong> Loại có dây đeo cổ trong suốt để chụp ảnh, quay video bơi lội an toàn.</div>
            </li>
            <li>
              <span class="c-icon">🏊</span>
              <div><strong>Đồ bơi & Kính bơi:</strong> Thỏa sức lặn ngắm suối trong vắt và bơi dưới chân thác lớn.</div>
            </li>
            <li>
              <span class="c-icon">🧴</span>
              <div><strong>Kem chống nắng & xịt côn trùng:</strong> Mũ lưỡi trai, bảo vệ da khi đi qua rừng.</div>
            </li>
            <li>
              <span class="c-icon">🍫</span>
              <div><strong>Đồ ăn vặt nạp năng lượng nhanh:</strong> Socola, kẹo gừng, bánh ngọt, gel năng lượng.</div>
            </li>
            <li>
              <span class="c-icon">🪥</span>
              <div><strong>Đồ vệ sinh cá nhân:</strong> Bàn chải, khăn mặt (đặc biệt cho ai chọn PA 2 ngủ đêm tại Farm).</div>
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
              <div><strong>Giày leo núi chống nước (Gore-Tex):</strong> Nước suối tràn vào sẽ đọng kín bên trong, nặng như đeo 2 xô nước vào chân.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>Quần jean / bò dày:</strong> Ngấm nước cực nặng, lâu khô và cọ xát gây rát da khi di chuyển.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>Trang sức quý giá, nhẫn vàng:</strong> Áp lực dòng nước lạnh và hoạt động leo trèo rất dễ làm tuột trôi xuống đáy suối sâu.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>Dép lê, dép lào xỏ ngón:</strong> Trơn trượt cực kỳ nguy hiểm trên đá rêu phong, dòng suối cuốn trôi ngay lập tức.</div>
            </li>
            <li>
              <span class="c-icon">❌</span>
              <div><strong>Ví tiền dày & giấy tờ không cần thiết:</strong> Chỉ cần mang CCCD và một ít tiền mặt, đồ đạc có giá trị nên gửi tại lễ tân Farm.</div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </section>"""

# Inject CSS before </style>
html = html.replace('</style>', packing_css + '\n  </style>')

# Inject HTML right before FAQS & PACKING LIST
target_faq = '  <!-- FAQS & PACKING LIST -->'
if target_faq in html:
    html = html.replace(target_faq, packing_html + '\n\n' + target_faq)
    print("Inserted Packing Section before FAQ!")
else:
    print("target_faq not found, appending before vote section")

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(base_dir, "template.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Packing checklist added successfully!")

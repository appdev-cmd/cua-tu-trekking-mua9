# -*- coding: utf-8 -*-
import os

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "template.html"), "r", encoding="utf-8") as f:
    tpl = f.read()

# 1. Update brand logo src to images/logo-100-days.jpg
tpl = tpl.replace('{{LOGO_B64_PLACEHOLDER}}', 'images/logo-100-days.jpg')
tpl = tpl.replace('{{IMG_B64_PLACEHOLDER}}', 'images/mam-com-suoi.jpg')

# 2. Add custom CSS for hero showcase, gallery grid, preview thumbnails, and lightbox
extra_css = """
    /* Hero Showcase Card */
    .hero-showcase-card {
      background: rgba(255, 255, 255, 0.08);
      backdrop-filter: blur(16px);
      border: 2px solid rgba(255, 255, 255, 0.18);
      border-radius: var(--radius-lg);
      padding: 16px;
      box-shadow: 0 20px 40px rgba(0,0,0,0.3);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .hero-main-photo-wrap {
      position: relative;
      border-radius: var(--radius-md);
      overflow: hidden;
      cursor: pointer;
      box-shadow: 0 8px 24px rgba(0,0,0,0.25);
      aspect-ratio: 16 / 10;
      border: 2px solid rgba(255, 255, 255, 0.2);
    }
    .hero-main-photo {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }
    .hero-main-photo-wrap:hover .hero-main-photo {
      transform: scale(1.05);
    }
    .hero-photo-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(13, 92, 62, 0.92);
      backdrop-filter: blur(8px);
      color: #fde047;
      font-size: 0.78rem;
      font-weight: 800;
      padding: 5px 12px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(253, 224, 71, 0.4);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .hero-logo-floating {
      position: absolute;
      bottom: 12px;
      right: 12px;
      width: 58px;
      height: 58px;
      border-radius: 50%;
      border: 3px solid var(--amber);
      overflow: hidden;
      box-shadow: 0 4px 15px rgba(0,0,0,0.4);
      background: #000;
      z-index: 2;
    }
    .hero-logo-floating img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .hero-thumbs-row {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 8px;
    }
    .hero-thumb {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      aspect-ratio: 4 / 3;
      cursor: pointer;
      border: 1px solid rgba(255,255,255,0.2);
      transition: all 0.2s ease;
    }
    .hero-thumb:hover {
      transform: translateY(-2px);
      border-color: var(--amber);
      box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
    }
    .hero-thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .hero-thumb span {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(to top, rgba(0,0,0,0.85), transparent);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 6px;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .hero-badge-sub {
      background: rgba(0,0,0,0.25);
      border-radius: 8px;
      padding: 8px 12px;
      font-size: 0.8rem;
      color: #f1f5f9;
      text-align: center;
      line-height: 1.4;
    }

    /* Photo Gallery Section */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 22px;
      margin-top: 15px;
    }
    @media (max-width: 900px) {
      .gallery-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }
    @media (max-width: 600px) {
      .gallery-grid {
        grid-template-columns: 1fr;
      }
    }
    .gallery-card {
      background: #ffffff;
      border-radius: var(--radius-md);
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--gray-200);
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      cursor: pointer;
    }
    .gallery-card:hover {
      transform: translateY(-6px);
      box-shadow: var(--shadow-lg);
      border-color: var(--primary-light);
    }
    .gallery-img-wrap {
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 11;
      overflow: hidden;
      background: #0f172a;
    }
    .gallery-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.4s ease;
    }
    .gallery-card:hover .gallery-img {
      transform: scale(1.06);
    }
    .gallery-badge {
      position: absolute;
      top: 12px;
      left: 12px;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(6px);
      color: #fef08a;
      font-size: 0.74rem;
      font-weight: 800;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      border: 1px solid rgba(255, 255, 255, 0.2);
    }
    .gallery-zoom-hint {
      position: absolute;
      bottom: 10px;
      right: 10px;
      background: rgba(0, 0, 0, 0.65);
      color: #fff;
      font-size: 0.72rem;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      backdrop-filter: blur(4px);
      opacity: 0.85;
    }
    .gallery-body {
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      flex: 1;
    }
    .gallery-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--dark);
      margin-bottom: 6px;
      line-height: 1.35;
    }
    .gallery-desc {
      font-size: 0.88rem;
      color: var(--gray-600);
      line-height: 1.5;
    }

    /* Option Card Previews */
    .opt-preview-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      margin: 16px 0 12px 0;
      padding: 10px;
      background: var(--gray-50);
      border-radius: var(--radius-sm);
      border: 1px solid var(--gray-200);
    }
    .opt-preview-item {
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      aspect-ratio: 4 / 3;
      cursor: pointer;
      border: 1px solid var(--gray-200);
    }
    .opt-preview-item img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.2s ease;
    }
    .opt-preview-item:hover img {
      transform: scale(1.08);
    }
    .opt-preview-item span {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(0,0,0,0.75);
      color: #fff;
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 4px;
      text-align: center;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Lightbox Modal */
    .lightbox {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 99999;
      background: rgba(0, 0, 0, 0.92);
      backdrop-filter: blur(10px);
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      transition: opacity 0.25s ease;
    }
    .lightbox.active {
      display: flex;
      opacity: 1;
    }
    .lightbox-container {
      position: relative;
      max-width: 92vw;
      max-height: 88vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      animation: lightboxPop 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes lightboxPop {
      from { transform: scale(0.92); opacity: 0; }
      to { transform: scale(1); opacity: 1; }
    }
    .lightbox-container img {
      max-width: 90vw;
      max-height: 76vh;
      object-fit: contain;
      border-radius: 12px;
      box-shadow: 0 15px 45px rgba(0,0,0,0.6);
      border: 2px solid rgba(255, 255, 255, 0.25);
    }
    .lightbox-caption {
      margin-top: 12px;
      color: #f1f5f9;
      font-size: 0.95rem;
      font-weight: 600;
      text-align: center;
      background: rgba(0, 0, 0, 0.6);
      padding: 6px 16px;
      border-radius: var(--radius-full);
      max-width: 90vw;
    }
    .lightbox-close {
      position: absolute;
      top: 20px;
      right: 25px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.2);
      border: 1px solid rgba(255, 255, 255, 0.4);
      color: #fff;
      font-size: 28px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: background 0.2s ease;
      z-index: 100000;
    }
    .lightbox-close:hover {
      background: rgba(225, 29, 72, 0.85);
    }
"""

tpl = tpl.replace('</style>', extra_css + '\n  </style>')

# 3. Replace Hero Right Column
old_hero_right = """        <!-- Logo Card Right Column -->
        <div>
          <div class="hero-logo-card">
            <img src="images/logo-100-days.jpg" alt="100-Day Challenge: For Money - Not For Justice" class="hero-logo-img" />
            <div class="hero-logo-title">100-DAY CHALLENGE</div>
            <div class="hero-logo-sub">FOR MONEY - NOT FOR JUSTICE</div>
            <p style="font-size: 0.85rem; color: #cbd5e1; margin-top: 8px;">
              Chúc mừng các chiến binh đã hoàn thành chặng đường Mùa 9 xuất sắc!
            </p>
          </div>
        </div>"""

new_hero_right = """        <!-- Hero Right Column: Visual Showcase -->
        <div>
          <div class="hero-showcase-card">
            <div class="hero-main-photo-wrap" onclick="openLightbox('images/cua-tu-cheo-sup-tam-suoi.jpg', 'Chèo SUP & Bơi lội dưới chân thác Cửa Tử - Trải nghiệm cực đã cho dân chạy bộ & bơi lội')">
              <img src="images/cua-tu-cheo-sup-tam-suoi.jpg" alt="Chèo SUP bơi lội Suối Cửa Tử" class="hero-main-photo" />
              <div class="hero-photo-badge">
                <span class="dot"></span> BƠI LỘI & CHÈO SUP DƯỚI THÁC
              </div>
              <div class="hero-logo-floating">
                <img src="images/logo-100-days.jpg" alt="Logo Mùa 9" />
              </div>
            </div>
            <div class="hero-thumbs-row">
              <div class="hero-thumb" onclick="openLightbox('images/cua-tu-truot-thac.jpg', 'Máng trượt thác tự nhiên triệu năm lao vút xuống hồ xanh ngọc')">
                <img src="images/cua-tu-truot-thac.jpg" alt="Trượt thác Cửa Tử" />
                <span>🌊 Trượt máng đá</span>
              </div>
              <div class="hero-thumb" onclick="openLightbox('images/cua-tu-dong-doi-vuot-suoi.jpg', 'Đồng đội dìu nhau vượt suối đá rêu phong')">
                <img src="images/cua-tu-dong-doi-vuot-suoi.jpg" alt="Đồng đội vượt suối" />
                <span>🥾 Băng suối</span>
              </div>
              <div class="hero-thumb" onclick="openLightbox('images/mam-com-suoi.jpg', 'Mâm cơm đãi chiến binh bên suối')">
                <img src="images/mam-com-suoi.jpg" alt="Mâm cơm rừng suối Cửa Tử" />
                <span>🍗 Ăn mâm rừng</span>
              </div>
            </div>
            <div class="hero-badge-sub">
              🏆 <strong>OFFLINE MÙA 9:</strong> Bơi lội & trekking xả hơi - Gắn kết đồng đội - Chi phí chia đều!
            </div>
          </div>
        </div>"""

if old_hero_right in tpl:
    tpl = tpl.replace(old_hero_right, new_hero_right)
else:
    print("Could not find old_hero_right directly, trying alternative search")

# 4. Insert Photo Gallery Section before OPTIONS COMPARISON SECTION
gallery_section = """
  <!-- REAL PHOTOS GALLERY SECTION -->
  <section class="section" id="gallery-section" style="background: white;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">📸 ALBUM ẢNH TRẢI NGHIỆM THỰC TẾ</span>
        <h2 class="section-title">Khám Phá Cung Suối Cửa Tử Tuyệt Đẹp</h2>
        <p class="section-desc">
          Tận mắt chiêm ngưỡng những trải nghiệm bơi lội, vượt thác và ẩm thực hoang sơ đang chờ đón các chiến binh Mùa 9 <em>(Bấm vào từng ảnh để phóng to)</em>
        </p>
      </div>

      <div class="gallery-grid">
        <!-- Photo 1: Chèo SUP & Bơi lội -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-cheo-sup-tam-suoi.jpg', 'Chèo SUP & Bơi lội tự do dưới thác Cửa Tử - Nước trong vắt, bọt tung trắng xóa')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-cheo-sup-tam-suoi.jpg" alt="Chèo SUP tắm suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🏊‍♂️ THỎA SỨC BƠI LỘI & SUP</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Chèo SUP & Bơi Lội Tự Do Dưới Thác Nước</h3>
            <p class="gallery-desc">Mặt hồ trong vắt nhìn tận đáy, dòng nước nguồn mát rượi 20-22°C từ dãy Tam Đảo. Thỏa mãn đam mê bơi lội sau 100 ngày khổ luyện, flycam ghi lại trọn vẹn những pha pose dáng đỉnh chóp!</p>
          </div>
        </div>

        <!-- Photo 2: Trượt thác tự nhiên -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-truot-thac.jpg', 'Máng trượt thác đá tự nhiên triệu năm lao vút xuống hồ xanh ngọc bích')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-truot-thac.jpg" alt="Máng trượt đá tự nhiên Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">⚡ CẢM GIÁC MẠNH AN TOÀN</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Máng Trượt Đá Triệu Năm Lao Xuống Hồ Ngọc</h3>
            <p class="gallery-desc">Được dòng nước suối mài nhẵn qua hàng triệu năm, bạn chỉ cần mặc áo phao và buông mình trượt vèo xuống hồ nước ngọc bích – cảm giác sảng khoái vỡ òa khó quên!</p>
          </div>
        </div>

        <!-- Photo 3: Thác nước hùng vĩ -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-thac-nuoc-hung-vi.jpg', 'Dòng thác nước 2 tầng Cửa Tử hùng vĩ giữa vách đá rêu phong Đông Tam Đảo')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-thac-nuoc-hung-vi.jpg" alt="Thác nước Cửa Tử hùng vĩ" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🏞️ THẮNG CẢNH HOANG SƠ</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Thác Nước Cửa Tử Hùng Vĩ Tung Bọt Trắng</h3>
            <p class="gallery-desc">Dòng thác đổ rì rầm giữa hai vách đá rêu phong cổ thụ. Không khí trong lành, mát rượi, là background 'sống ảo' triệu view cho toàn đoàn.</p>
          </div>
        </div>

        <!-- Photo 4: Đồng đội vượt suối -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-dong-doi-vuot-suoi.jpg', 'Đồng đội dìu nhau vượt suối đá ghềnh thác - Tinh thần 100 ngày keo sơn')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-dong-doi-vuot-suoi.jpg" alt="Đồng đội vượt suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🤝 TINH THẦN ĐỒNG ĐỘI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Lội Suối Băng Rừng – Dìu Nhau Vượt Đá</h3>
            <p class="gallery-desc">Những đoạn lội suối róc rách nước ngập qua gối, anh em hỗ trợ nhau từng bước chân vững chãi. Tinh thần đồng đội Mùa 9 càng thêm keo sơn, gắn kết.</p>
          </div>
        </div>

        <!-- Photo 5: Rừng nguyên sinh -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-cung-duong-nguyen-sinh.jpg', 'Tán rừng nguyên sinh Đông Tam Đảo với chuối rừng và bãi đá khổng lồ')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-cung-duong-nguyen-sinh.jpg" alt="Rừng nguyên sinh suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🌿 DETOX TÂM HỒN</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Rừng Nguyên Sinh Hoang Sơ Tuyệt Mỹ</h3>
            <p class="gallery-desc">Thảm thực vật nguyên sinh trù phú, những rặng chuối rừng ngút ngàn và bãi đá cuội khổng lồ – giúp xua tan 100% căng thẳng, âu lo của nhịp sống phố thị.</p>
          </div>
        </div>

        <!-- Photo 6: Mâm cơm bên suối -->
        <div class="gallery-card" onclick="openLightbox('images/mam-com-suoi.jpg', 'Mâm cơm dã ngoại 6 người bày trên lá dong giữa bờ suối róc rách')">
          <div class="gallery-img-wrap">
            <img src="images/mam-com-suoi.jpg" alt="Mâm cơm rừng đãi chiến binh bên suối" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🍗 ĐẠI TIỆC DÃ NGOẠI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Mâm Cơm Đãi Chiến Binh Bên Dòng Suối</h3>
            <p class="gallery-desc">Gà đồi nướng than hoa vàng ươm, ba chỉ quay giòn bì, xôi nếp nương thơm nức bày trên lá dong giữa dòng suối đá mát lành – bữa tiệc nhớ đời!</p>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

target_options_marker = '  <!-- OPTIONS COMPARISON SECTION -->'
if target_options_marker in tpl:
    tpl = tpl.replace(target_options_marker, gallery_section + '\n' + target_options_marker)
else:
    print("Could not find target_options_marker")

# 5. Add preview thumbnails in Option 1 and Option 2 cards
old_opt1_price = """            <div class="price-box">
              <div class="price-label">Chi phí ước tính (Kinh phí chia đều)</div>
              <div class="price-val green">~790.000 <span style="font-size: 1rem;">đ/người</span></div>
              <div class="price-note">* Giá lẻ 990k - Đoàn đông chia đều sòng phẳng cho mỗi người tham gia</div>
            </div>"""

new_opt1_price = """            <div class="price-box">
              <div class="price-label">Chi phí ước tính (Kinh phí chia đều)</div>
              <div class="price-val green">~790.000 <span style="font-size: 1rem;">đ/người</span></div>
              <div class="price-note">* Giá lẻ 990k - Đoàn đông chia đều sòng phẳng cho mỗi người tham gia</div>
            </div>

            <!-- Preview Photos Option 1 -->
            <div class="opt-preview-grid">
              <div class="opt-preview-item" onclick="openLightbox('images/cua-tu-truot-thac.jpg', 'Máng trượt thác tự nhiên Cửa Tử 1')">
                <img src="images/cua-tu-truot-thac.jpg" alt="Trượt máng đá" />
                <span>Máng trượt đá</span>
              </div>
              <div class="opt-preview-item" onclick="openLightbox('images/cua-tu-dong-doi-vuot-suoi.jpg', 'Lội suối băng rừng Cửa Tử')">
                <img src="images/cua-tu-dong-doi-vuot-suoi.jpg" alt="Lội suối đá" />
                <span>Lội suối đá</span>
              </div>
              <div class="opt-preview-item" onclick="openLightbox('images/mam-com-suoi.jpg', 'Mâm cỗ gà nướng bên suối')">
                <img src="images/mam-com-suoi.jpg" alt="Ăn mâm suối" />
                <span>Ăn mâm suối</span>
              </div>
            </div>"""

tpl = tpl.replace(old_opt1_price, new_opt1_price)

old_opt2_price = """            <div class="price-box">
              <div class="price-label">Chi phí ước tính (Kinh phí chia đều)</div>
              <div class="price-val amber">~1.800.000 <span style="font-size: 1rem;">đ/người</span></div>
              <div class="price-note">* Trọn gói 2N1Đ - Toàn bộ kinh phí chia đều công bằng cho đoàn</div>
            </div>"""

new_opt2_price = """            <div class="price-box">
              <div class="price-label">Chi phí ước tính (Kinh phí chia đều)</div>
              <div class="price-val amber">~1.800.000 <span style="font-size: 1rem;">đ/người</span></div>
              <div class="price-note">* Trọn gói 2N1Đ - Toàn bộ kinh phí chia đều công bằng cho đoàn</div>
            </div>

            <!-- Preview Photos Option 2 -->
            <div class="opt-preview-grid">
              <div class="opt-preview-item" onclick="openLightbox('images/cua-tu-cheo-sup-tam-suoi.jpg', 'Chèo SUP & Bơi lội dưới chân thác Cửa Tử')">
                <img src="images/cua-tu-cheo-sup-tam-suoi.jpg" alt="Chèo SUP tắm suối" />
                <span>Bơi & Chèo SUP</span>
              </div>
              <div class="opt-preview-item" onclick="openLightbox('images/cua-tu-thac-nuoc-hung-vi.jpg', 'Thác nước 2 tầng Đông Tam Đảo')">
                <img src="images/cua-tu-thac-nuoc-hung-vi.jpg" alt="Thác nước hùng vĩ" />
                <span>Thác hùng vĩ</span>
              </div>
              <div class="opt-preview-item" onclick="openLightbox('images/cua-tu-cung-duong-nguyen-sinh.jpg', 'Khám phá rừng nguyên sinh Đông Tam Đảo')">
                <img src="images/cua-tu-cung-duong-nguyen-sinh.jpg" alt="Rừng nguyên sinh" />
                <span>Trek 10 cửa suối</span>
              </div>
            </div>"""

tpl = tpl.replace(old_opt2_price, new_opt2_price)

# 6. Make food image clickable for Lightbox
tpl = tpl.replace(
    '<div class="food-image-wrapper">',
    '<div class="food-image-wrapper" style="cursor: pointer;" onclick="openLightbox(\'images/mam-com-suoi.jpg\', \'Mâm cơm dã ngoại 6 người phục vụ thực tế bên suối Cửa Tử\')">'
)

# 7. Add Lightbox Modal & JS functions before </body>
lightbox_html = """
  <!-- Lightbox Modal Component -->
  <div id="imageLightbox" class="lightbox" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox(event)" aria-label="Đóng">&times;</button>
    <div class="lightbox-container" onclick="event.stopPropagation()">
      <img id="lightboxImg" src="" alt="Hình ảnh phóng to Suối Cửa Tử" />
      <div id="lightboxCaption" class="lightbox-caption"></div>
    </div>
  </div>

  <script>
    function openLightbox(src, caption) {
      const modal = document.getElementById('imageLightbox');
      const img = document.getElementById('lightboxImg');
      const cap = document.getElementById('lightboxCaption');
      img.src = src;
      cap.innerText = caption || '';
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }

    function closeLightbox(event) {
      const modal = document.getElementById('imageLightbox');
      modal.classList.remove('active');
      document.body.style.overflow = 'auto';
    }

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') {
        closeLightbox();
      }
    });
  </script>
"""

tpl = tpl.replace('</body>', lightbox_html + '\n</body>')

# Write back to index.html and template.html
with open(os.path.join(base_dir, "template.html"), "w", encoding="utf-8") as f:
    f.write(tpl)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(tpl)

print("Generated enhanced index.html and template.html successfully!")

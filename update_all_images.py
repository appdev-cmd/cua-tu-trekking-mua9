# -*- coding: utf-8 -*-
import os
import re

base_dir = r"C:\Users\hoang\.gemini\antigravity\scratch\trekking-cua-tu"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove the preview photos in Option 1
# Remove <!-- Preview Photos Option 1 --> ... </div>
pattern_opt1_preview = r'<!-- Preview Photos Option 1 -->\s*<div class="opt-preview-grid">[\s\S]*?</div>\s*</div>'
html = re.sub(pattern_opt1_preview, '', html)

# If there is any remaining opt-preview-grid in option cards, remove it
pattern_opt_grid = r'<div class="opt-preview-grid">[\s\S]*?</div>'
html = re.sub(pattern_opt_grid, '', html)

# 2. Update Gallery Section to include all 11 photos in an elegant responsive grid
new_gallery_section = """  <!-- REAL PHOTOS GALLERY SECTION -->
  <section class="section" id="gallery-section" style="background: white;">
    <div class="container">
      <div class="section-header">
        <span class="section-tag">📸 THƯ VIỆN ẢNH TRẢI NGHIỆM THỰC TẾ</span>
        <h2 class="section-title">Khám Phá Toàn Cảnh Cung Suối Cửa Tử Tuyệt Đẹp</h2>
        <p class="section-desc">
          Tận mắt chiêm ngưỡng những khoảnh khắc bơi lội, vượt thác, băng rừng rợp bóng mát và ẩm thực dã ngoại đang chờ đón bạn <em>(Bấm vào bất kỳ ảnh nào để phóng to chi tiết)</em>
        </p>
      </div>

      <div class="gallery-grid">
        <!-- Photo 1: Chèo SUP & Bơi lội -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-cheo-sup-tam-suoi.jpg', 'Chèo SUP & Bơi lội tự do dưới thác Cửa Tử - Nước trong vắt, bọt tung trắng xóa, flycam ghi hình')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-cheo-sup-tam-suoi.jpg" alt="Chèo SUP tắm suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🏊‍♂️ BƠI LỘI & CHÈO SUP</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Chèo SUP & Bơi Lội Thỏa Thích Dưới Thác Nước</h3>
            <p class="gallery-desc">Mặt hồ trong vắt nhìn tận đáy, dòng nước nguồn mát rượi 20-22°C từ dãy Tam Đảo. Thỏa mãn đam mê bơi lội sau 100 ngày khổ luyện, flycam ghi lại trọn vẹn những pha pose dáng đỉnh chóp!</p>
          </div>
        </div>

        <!-- Photo 2: Trượt thác tự nhiên -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-truot-thac.jpg', 'Máng trượt thác đá tự nhiên triệu năm lao vút xuống hồ nước xanh ngọc bích')">
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
            <span class="gallery-badge">🏞️ KỲ QUAN ĐÔNG TAM ĐẢO</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Thác Nước Cửa Tử Hùng Vĩ Tung Bọt Trắng</h3>
            <p class="gallery-desc">Dòng thác đổ rì rầm giữa hai vách đá rêu phong cổ thụ. Không khí trong lành, mát rượi, là background 'sống ảo' triệu view cho toàn đoàn.</p>
          </div>
        </div>

        <!-- Photo 4: Porter đồng hành lội suối -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-porter-dong-hanh-loi-suoi.jpg', 'Đội ngũ porter bản địa mang vác áo phao trợ nổi đồng hành sát sườn đảm bảo an toàn tuyệt đối')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-porter-dong-hanh-loi-suoi.jpg" alt="Porter đồng hành lội suối an toàn" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🦺 AN TOÀN TUYỆT ĐỐI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Lội Suối An Toàn – Porter Bản Địa Theo Sát</h3>
            <p class="gallery-desc">100% người tham gia được trang bị áo phao trợ nổi đạt chuẩn, đội ngũ porter người địa phương dày kinh nghiệm vác đồ và hỗ trợ sát sườn từng bước qua dòng nước trong vắt.</p>
          </div>
        </div>

        <!-- Photo 5: Trekking dưới tán rừng già -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-trekking-duoi-tan-rung.jpg', 'Cung đường trekking rợp bóng mát dưới tán rừng nguyên sinh Đông Tam Đảo')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-trekking-duoi-tan-rung.jpg" alt="Trekking dưới tán rừng nguyên sinh" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🥾 RỢP BÓNG RỪNG GIÀ</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Trekking Mát Rượi Dưới Tán Rừng Nguyên Sinh</h3>
            <p class="gallery-desc">Lối mòn băng qua rừng già Đông Tam Đảo được che phủ bởi tầng tầng lớp lớp tán cây cổ thụ, khí hậu trong lành thanh lọc lá phổi, không lo nắng gắt.</p>
          </div>
        </div>

        <!-- Photo 6: Đồng đội dìu nhau vượt suối -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-dong-doi-vuot-suoi.jpg', 'Đồng đội dìu nhau vượt suối đá ghềnh thác - Tinh thần 100 ngày keo sơn')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-dong-doi-vuot-suoi.jpg" alt="Đồng đội vượt suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🤝 TINH THẦN ĐỒNG ĐỘI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Lội Suối Băng Ghềnh – Gắn Kết Chiến Binh</h3>
            <p class="gallery-desc">Những đoạn lội suối róc rách nước ngập qua gối, anh em hỗ trợ nhau từng bước chân vững chãi. Tinh thần đồng đội Mùa 9 càng thêm keo sơn, gắn kết.</p>
          </div>
        </div>

        <!-- Photo 7: Lối mòn rêu phong -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-duong-mon-reu-phong.jpg', 'Đường mòn đá rêu phong xanh mướt mát lành tĩnh lặng')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-duong-mon-reu-phong.jpg" alt="Lối mòn đá rêu phong" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🌿 LỐI MÒN XANH MƯỚT</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Đường Mòn Đá Rêu Phong & Cổ Thụ Kỳ Vĩ</h3>
            <p class="gallery-desc">Những bậc đá phủ rêu xanh cổ kính uốn lượn theo sườn núi, không gian tĩnh lặng chỉ có tiếng chim hót líu lo và tiếng gió rừng rì rào.</p>
          </div>
        </div>

        <!-- Photo 8: Nắng chiếu qua tán lá cọ rừng -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-nang-chieu-tan-la-rung.jpg', 'Ánh nắng vàng len lỏi qua tán cọ rừng nhiệt đới Đông Tam Đảo')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-nang-chieu-tan-la-rung.jpg" alt="Nắng qua tán cọ rừng" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">☀️ NẮNG RỪNG NHIỆT ĐỚI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Nắng Vàng Len Lỏi Qua Tán Cọ Rừng</h3>
            <p class="gallery-desc">Cảnh sắc thiên nhiên Đông Tam Đảo tráng lệ, ánh nắng xuyên qua những tán lá cọ khổng lồ tạo nên khung cảnh điện ảnh tuyệt đẹp.</p>
          </div>
        </div>

        <!-- Photo 9: Rừng dương xỉ nguyên sinh -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-rung-duong-xi-nguyen-sinh.jpg', 'Tán dương xỉ cổ thụ đại ngàn Đông Tam Đảo - Khung cảnh hoang dã')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-rung-duong-xi-nguyen-sinh.jpg" alt="Rừng dương xỉ nguyên sinh" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🌲 TÁN DƯƠNG XỈ CỔ THỤ</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Rừng Dương Xỉ Khổng Lồ Cổ Thụ</h3>
            <p class="gallery-desc">Góc nhìn ngoạn mục qua tán dương xỉ nguyên sinh hàng trăm năm tuổi, cảm giác như bước vào một thế giới Jurassic hoang sơ huyền bí.</p>
          </div>
        </div>

        <!-- Photo 10: Rừng nguyên sinh & bãi đá tảng -->
        <div class="gallery-card" onclick="openLightbox('images/cua-tu-cung-duong-nguyen-sinh.jpg', 'Tán rừng nguyên sinh Đông Tam Đảo với chuối rừng và bãi đá tảng khổng lồ')">
          <div class="gallery-img-wrap">
            <img src="images/cua-tu-cung-duong-nguyen-sinh.jpg" alt="Rừng nguyên sinh suối Cửa Tử" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🪨 BÃI ĐÁ TẢNG HÙNG VĨ</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Bãi Đá Tảng Hùng Vĩ & Cây Rừng Đại Ngàn</h3>
            <p class="gallery-desc">Thảm thực vật nguyên sinh trù phú, những rặng chuối rừng ngút ngàn và bãi đá cuội khổng lồ – giúp xua tan 100% căng thẳng, âu lo của nhịp sống phố thị.</p>
          </div>
        </div>

        <!-- Photo 11: Mâm cơm bên suối -->
        <div class="gallery-card" onclick="openLightbox('images/mam-com-suoi.jpg', 'Mâm cơm dã ngoại 6 người bày trên lá dong giữa bờ suối róc rách')">
          <div class="gallery-img-wrap">
            <img src="images/mam-com-suoi.jpg" alt="Mâm cơm rừng đãi chiến binh bên suối" class="gallery-img" loading="lazy" />
            <span class="gallery-badge">🍗 ĐẠI TIỆC DÃ NGOẠI</span>
            <span class="gallery-zoom-hint">🔍 Phóng to</span>
          </div>
          <div class="gallery-body">
            <h3 class="gallery-title">Mâm Cơm Đãi Chiến Binh Bên Dòng Suối</h3>
            <p class="gallery-desc">Gà đồi nướng than hoa vàng rộm, ba chỉ quay giòn bì, xôi nếp nương thơm nức bày trên lá dong giữa dòng suối đá mát lành – bữa tiệc nhớ đời!</p>
          </div>
        </div>
      </div>
    </div>
  </section>"""

# Replace the existing gallery section
pattern_gallery = r'<!-- REAL PHOTOS GALLERY SECTION -->[\s\S]*?</section>'
if re.search(pattern_gallery, html):
    html = re.sub(pattern_gallery, new_gallery_section, html)
    print("Replaced gallery section successfully!")
else:
    print("Pattern gallery not found, checking options marker...")
    target_options_marker = '  <!-- OPTIONS COMPARISON SECTION -->'
    if target_options_marker in html:
        html = html.replace(target_options_marker, new_gallery_section + '\n' + target_options_marker)

# 3. Update Hero Showcase Card thumbs to have 4 balanced items
old_hero_showcase = r'<div class="hero-showcase-card">[\s\S]*?</div>\s*</div>\s*</div>'
new_hero_showcase = """<div class="hero-showcase-card">
            <div class="hero-main-photo-wrap" onclick="openLightbox('images/cua-tu-cheo-sup-tam-suoi.jpg', 'Chèo SUP & Bơi lội dưới chân thác Cửa Tử - Trải nghiệm cực đã cho dân chạy bộ & bơi lội')">
              <img src="images/cua-tu-cheo-sup-tam-suoi.jpg" alt="Chèo SUP bơi lội Suối Cửa Tử" class="hero-main-photo" />
              <div class="hero-photo-badge">
                <span class="dot"></span> BƠI LỘI & CHÈO SUP DƯỚI THÁC
              </div>
              <div class="hero-logo-floating">
                <img src="images/logo-100-days.jpg" alt="Logo Mùa 9" />
              </div>
            </div>
            <div class="hero-thumbs-row" style="grid-template-columns: repeat(4, 1fr);">
              <div class="hero-thumb" onclick="openLightbox('images/cua-tu-truot-thac.jpg', 'Máng trượt thác tự nhiên triệu năm lao vút xuống hồ xanh ngọc')">
                <img src="images/cua-tu-truot-thac.jpg" alt="Trượt thác Cửa Tử" />
                <span>🌊 Trượt máng</span>
              </div>
              <div class="hero-thumb" onclick="openLightbox('images/cua-tu-porter-dong-hanh-loi-suoi.jpg', 'Porter bản địa mang vác áo phao trợ nổi đồng hành sát sườn')">
                <img src="images/cua-tu-porter-dong-hanh-loi-suoi.jpg" alt="Lội suối an toàn" />
                <span>🦺 An toàn</span>
              </div>
              <div class="hero-thumb" onclick="openLightbox('images/cua-tu-trekking-duoi-tan-rung.jpg', 'Trekking mát rượi dưới tán rừng già nguyên sinh')">
                <img src="images/cua-tu-trekking-duoi-tan-rung.jpg" alt="Trek rừng mát" />
                <span>🥾 Trek rừng</span>
              </div>
              <div class="hero-thumb" onclick="openLightbox('images/mam-com-suoi.jpg', 'Mâm cơm đãi chiến binh bên suối')">
                <img src="images/mam-com-suoi.jpg" alt="Mâm cơm rừng suối Cửa Tử" />
                <span>🍗 Mâm suối</span>
              </div>
            </div>
            <div class="hero-badge-sub">
              🏆 <strong>OFFLINE MÙA 9:</strong> Bơi lội & trekking xả hơi - Gắn kết đồng đội - Chi phí chia đều!
            </div>
          </div>
        </div>
      </div>"""

html = re.sub(old_hero_showcase, new_hero_showcase, html)

# 4. Enhance the FAQ item for "Không biết bơi có đi được không?" with a small proof photo card
old_swim_faq = """        <div class="feature-card">
          <h3 style="color: var(--primary);">🏊 Không biết bơi có đi được không?</h3>
          <p>
            <strong>Chắc chắn 100% đi được!</strong> Ban tổ chức trang bị áo phao cứu sinh chất lượng cao có sức nổi cực tốt. Bạn chỉ cần thả lỏng người là nổi bồng bềnh, hơn nữa luôn có các anh porter địa phương bám sát hỗ trợ từng bước chân.
          </p>
        </div>"""

new_swim_faq = """        <div class="feature-card">
          <h3 style="color: var(--primary);">🏊 Không biết bơi có đi được không?</h3>
          <p>
            <strong>Chắc chắn 100% đi được!</strong> Ban tổ chức trang bị áo phao cứu sinh trợ nổi chất lượng cao. Bạn chỉ cần mặc áo phao là nổi bồng bềnh 100%, hơn nữa luôn có các anh porter bản địa dày kinh nghiệm đi kèm hỗ trợ từng bước chân.
          </p>
          <div style="margin-top: 10px; display: flex; align-items: center; gap: 10px; background: var(--gray-50); padding: 8px; border-radius: 8px; cursor: pointer; border: 1px solid var(--gray-200);" onclick="openLightbox('images/cua-tu-porter-dong-hanh-loi-suoi.jpg', 'Hình ảnh thực tế: Đội ngũ porter mang vác áo phao trợ nổi đồng hành sát sườn cùng đoàn lội suối')">
            <img src="images/cua-tu-porter-dong-hanh-loi-suoi.jpg" alt="Porter đồng hành an toàn" style="width: 60px; height: 45px; object-fit: cover; border-radius: 6px;" />
            <span style="font-size: 0.82rem; font-weight: 700; color: var(--primary);">📸 Xem hình ảnh thực tế: Porter kèm áo phao trợ nổi sát sườn đoàn ↗</span>
          </div>
        </div>"""

html = html.replace(old_swim_faq, new_swim_faq)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(base_dir, "template.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html and template.html successfully!")

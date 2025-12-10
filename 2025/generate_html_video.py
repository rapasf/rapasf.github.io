#!/usr/bin/env python3
"""
make_videos_html.py
Generates an HTML file with videos A01–A35 and solution modals.
"""

HTML_TEMPLATE_HEAD = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Video Clips A01-A35</title>
  <style>
    body { font-family: Arial, Helvetica, sans-serif; padding: 20px; }
    section { margin-bottom: 40px; }
    h2 { margin: 0 0 8px 0; }
    video { display: block; max-width: 100%; height: auto; }

    /* Button styling */
    .button-container { margin-top: 10px; }
    .btn {
      padding: 8px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 14px;
    }
    .btn:hover { background-color: #0056b3; }

    /* Modal styling */
    .modal {
      display: none;
      position: fixed;
      z-index: 1000;
      padding-top: 80px;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      background: rgba(0,0,0,0.6);
    }
    .modal-content {
      background: white;
      margin: auto;
      padding: 16px;
      border-radius: 8px;
      max-width: 600px;
    }
    .close-btn {
      float: right;
      font-size: 28px;
      cursor: pointer;
    }
    img { width: 100%; height: auto; }
  </style>

  <script>
    function openModal(id) {
      document.getElementById(id).style.display = "block";
    }
    function closeModal(id) {
      document.getElementById(id).style.display = "none";
    }
  </script>
</head>
<body>
  <h1>Clips A01 — A35</h1>
"""

HTML_TEMPLATE_TAIL = """
</body>
</html>
"""

def generate_block(index: int, cat = 'G') -> str:
    """
    Creates the video + button + modal HTML block for index 1..35.
    """
    heading = f"{cat}{index}"
    video_file = f"clips/{cat}{index:02d}.mp4"
    image_file = f"decisions/{cat}{index}.png"
    modal_id = f"imageModal{index}"

    block = f"""  <section>
    <h2>{heading}</h2>

    <video controls width="640">
      <source src="{video_file}" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <!-- Button -->
    <div class="button-container">
      <button class="btn" onclick="openModal('{modal_id}')">
        Show solution
      </button>
    </div>

    <!-- Modal -->
    <div id="{modal_id}" class="modal">
      <div class="modal-content">
        <span class="close-btn" onclick="closeModal('{modal_id}')">&times;</span>
        <img src="{image_file}" alt="{heading} Solution" />
      </div>
    </div>

  </section>
"""
    return block

def make_html(start=1, end=10, out_file="videos.html"):
    html = [HTML_TEMPLATE_HEAD]
    for i in range(start, end + 1):
        html.append(generate_block(i))
    html.append(HTML_TEMPLATE_TAIL)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(html))

    print(f"Generated: {out_file}")

if __name__ == "__main__":
    make_html()

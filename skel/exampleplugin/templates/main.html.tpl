{{ extends_base }}
{{ block_head }}
    <script type="application/javascript">
        $(document).ready(function() {

                $(".rs-collapsible-section .rs-detail-section-header").click(function()
                {
                        $(this).parent().toggleClass("collapsed expanded");
                });

        });
    </script>
{{ end }}
{{ block_title }}
 - Example Controller
{{ end }}
{{ block_sidebar }}
{{ end }}
{{ block_body }}
      <div class="rs-content">
          <div class="rs-detail-section">
            <div class="rs-detail-section-header">
              <h2 class="rs-page-title">Example Page with Example Form:</h2>
            </div>
            <div class="rs-detail-section-body">
              Example Controller
            </div>
          </div>
    </div>

{{ end }}

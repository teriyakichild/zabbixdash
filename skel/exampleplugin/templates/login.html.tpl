{% autoescape None %}
{{ extends_base }}
{{ block_title_login }}
{{ block_head }}
<script type="application/javascript">
$(document).ready(function() {
        
        $(".rs-tabs a").click(function()
        {
                this.blur();
                var content = $($(this).attr("href"));
                content.addClass("active").siblings(".active").removeClass("active");
                $(this).parent().addClass("active").siblings(".active").removeClass("active");
                return false;
        });
        
});
</script>
{{ end }}
{{ block_title }}
{{ end }}
{{ block_sidebar }}
{{ end }}
{{ block_body }}
  {{ if_error }}
    <div class="alert alert-error">
    {{ error }}
    </div>
  {{ end }}
<form class="form-horizontal" method="POST">
  <div class="control-group">
    <label class="control-label" for="username">Username</label>
    <div class="controls">
      <input type="text" id="username" name="username" placeholder="Username">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="Password">Password</label>
    <div class="controls">
      <input type="password" id="password" name="password" placeholder="Password">
    </div>
  </div>
  <div class="control-group">
    <div class="controls">
      <label class="checkbox">
        <input type="checkbox"> Remember me
      </label>
      <button type="submit" class="btn">Sign in</button>
    </div>
  </div>
</form>
{{ end }}

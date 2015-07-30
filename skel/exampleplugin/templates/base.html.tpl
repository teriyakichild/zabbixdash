{% autoescape None %}
<!DOCTYPE html>
<html>
<head>
	<title>{{ title }}</title>
	<meta name="viewport" content="width=device-width">
	<link rel="stylesheet" type="text/css" href="https://eafdbc63c97ce6bec9ef-b0a668e5876bef6fe25684caf71db405.ssl.cf1.rackcdn.com/v1-latest/canon.min.css">
	<script type="application/javascript" src="https://code.jquery.com/jquery-1.10.0.min.js"></script>
	<script type="application/javascript" src="https://eafdbc63c97ce6bec9ef-b0a668e5876bef6fe25684caf71db405.ssl.cf1.rackcdn.com/v1-latest/canon.min.js"></script>
        <script type="application/javascript">
            function toggle_view(name) {
                element = document.getElementById(name)
                if (element.classList.contains('hidden')) {
                    element.classList.remove('hidden')
                    element.classList.add('visible')
                } else {
                    element.classList.remove('visible')
                    element.classList.add('hidden')
                }
                return
            }
        </script>
        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
        {{ block_head_end }}
</head>

<body class="rs-responsive">
	<div class="rs-wrapper">
		<div class="rs-nav-utility">
			<div class="rs-container">
				<ul class="rs-nav rs-pull-right">
            <li class="rs-nav-item">
                {{ ifcurrent_user }}
                        <a class="rs-nav-link" href="/login">Login</a>
                {{ else_v }}
                      <li class="rs-dropdown rs-utility-dropdown">
                        <a class="rs-dropdown-toggle" onClick="toggle_view('dropdown')" href="javascript:void(0);">
                            User: {{ current_user }} <i class="rs-caret"></i>
                        </a>
                        <ul id="dropdown" class="rs-dropdown-menu hidden">
                          <li class="rs-divider"></li>
                          <li class="rs-dropdown-item">
                            <a class="rs-dropdown-link" href="/logout">Log Out</a>
                          </li>
                        </ul>
                      </li>
                {{ end }}
            </li>
				</ul>
			</div>
		</div>
		{{ block_nav }}
				<div class="rs-nav-primary" id="mainmenu">
					<div class="rs-container">
						<div class="rs-nav-brand">
							<a href="/"></a>
						</div>
						<ul class="rs-nav">
                                                    {{ for_name }}
							<li>{{ link_name }}</li>
                                                    {{ end }}
						</ul>
					</div>
				</div>
                {{ end }}
		<div class="rs-body">
			<div class="rs-container">
				<div class="rs-main">
					<div class="rs-content rs-panel">
						<div class="rs-inner">
							<h2 class="rs-page-title">{{ app_title }}</h2>
							{{ block_body }}

							{{ end }}
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="rs-push"></div>
	</div>
	<div class="rs-nav-footer">
		<div class="rs-container">
			<ul class="rs-nav">
                                <li class="rs-nav-item">{{ app_title }} v{{ version }}</li>
				<li class="rs-nav-item">&copy; Rackspace, US</li>
				<li class="rs-nav-item"><a class="rs-nav-link" href="http://www.rackspace.com/information/legal/websiteterms" target="blank">Website Terms</a>
				<li class="rs-nav-item"><a class="rs-nav-link" href="http://www.rackspace.com/information/legal/privacystatement" target="blank">Privacy Policy</a>
			</ul>
		</div>
	</div>
</body>
</html>

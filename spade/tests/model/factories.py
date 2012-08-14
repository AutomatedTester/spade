# Factories for testing objects
import factory

from datetime import datetime
from django.utils.timezone import utc
from hashlib import sha256
from spade.model import models

MOCK_DATE = datetime(2012, 6, 29, 21, 10, 24, 10848, tzinfo=utc)
MOCK_CSS_URL = (u"http://www.sammyliu.com/wp-content/themes/polaroid-perfect/"
                u"style.css")
MOCK_JS_URL = u"http://code.jquery.com/jquery-1.7.2.min.js"


class BatchFactory(factory.Factory):
    """ Batch model factory """
    FACTORY_FOR = models.Batch
    kickoff_time = datetime.now(utc)
    finish_time = datetime.now(utc)


class BatchUserAgentFactory(factory.Factory):
    """ Batch user agent factory """
    FACTORY_FOR = models.BatchUserAgent
    batch = factory.SubFactory(BatchFactory)
    ua_string = "Firefox / 5.0"


class SiteScanFactory(factory.Factory):
    """ Site scan model factory """
    FACTORY_FOR = models.SiteScan
    batch = factory.SubFactory(BatchFactory)
    site_url = u"http://www.mozilla.com"
    site_url_hash = sha256(site_url).hexdigest()


class URLScanFactory(factory.Factory):
    """ URL scan model factory """
    FACTORY_FOR = models.URLScan
    site_scan = factory.SubFactory(SiteScanFactory)
    page_url = u"http://www.mozilla.com"
    timestamp = MOCK_DATE
    page_url_hash = sha256("http://www.mozilla.com").hexdigest()


class UserAgentFactory(factory.Factory):
    """ User agent model factory """
    FACTORY_FOR = models.UserAgent
    ua_string = u"Firefox / 5.0"


class URLContentFactory(factory.Factory):
    """ URL Content model factory """
    FACTORY_FOR = models.URLContent
    url_scan = factory.SubFactory(URLScanFactory)
    user_agent = factory.SubFactory(BatchUserAgentFactory)
    raw_markup = u"<html>hello world</html>"
    headers = u""


class LinkedCSSFactory(factory.Factory):
    """ Linked CSS model factory """
    FACTORY_FOR = models.LinkedCSS
    url = MOCK_CSS_URL
    url_hash = sha256(MOCK_CSS_URL).hexdigest()
    raw_css = u"body{color:#000}"


class LinkedJSFactory(factory.Factory):
    """ Linked JS model factory """
    FACTORY_FOR = models.LinkedJS
    url = MOCK_JS_URL
    url_hash = sha256(MOCK_JS_URL).hexdigest()
    raw_js = u"document.write('hello world')"


class CSSRuleFactory(factory.Factory):
    """ CSS Rule model factory """
    FACTORY_FOR = models.CSSRule
    linkedcss = factory.SubFactory(LinkedCSSFactory)
    selector = "body"


class CSSPropertyFactory(factory.Factory):
    """ CSS Property model factory """
    FACTORY_FOR = models.CSSProperty
    rule = factory.SubFactory(CSSRuleFactory)
    prefix = ""
    name = "text-decoration"
    value = "none"


class BatchDataFactory(factory.Factory):
    """ Factory for batch data """
    FACTORY_FOR = models.BatchData
    batch = factory.SubFactory(BatchFactory)


class SiteScanDataFactory(factory.Factory):
    """ Factory for sitescan data """
    FACTORY_FOR = models.SiteScanData
    sitescan = factory.SubFactory(SiteScan)


class URLScanDataFactory(factory.Factory):
    """ Factory for urlscan data """
    FACTORY_FOR = models.URLScanData
    urlscan = factory.SubFactory(URLScan)


class URLContentDataFactory(factory.Factory):
    """ Factory for urlcontent data """
    FACTORY_FOR = models.URLContentData
    urlcontent = factory.SubFactory(URLContent)


class LinkedCSSDataFactory(factory.Factory):
    """ Factory for LinkedCSS data """
    FACTORY_FOR = models.LinkedCSSData
    linked_css = factory.SubFactory(LinkedCSS)

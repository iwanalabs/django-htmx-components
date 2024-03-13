from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            # "index",
            "active_search",
            "bulk_update",
            "cascading_selects",
            "click_to_edit",
            "click_to_load",
            "delete_row",
            "edit_row",
            "infinite_scroll",
            "inline_validation",
            "progress_bar",
        ]

    def location(self, item):
        return reverse(item)

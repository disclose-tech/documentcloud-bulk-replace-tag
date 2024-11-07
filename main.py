"""
This Add-On allows users to change the value of a tag in bulk
"""

from documentcloud.addon import SoftTimeOutAddOn


class BulkReplaceTag(SoftTimeOutAddOn):
    """An example Add-On for DocumentCloud."""

    def main(self):
        """The main add-on functionality goes here."""
        # fetch your add-on specific data

        key = self.data.get("key").strip()
        value = self.data.get("value").strip()
        add_if_missing = self.data.get("value")

        for document in self.get_documents():
            if key in document.data or add_if_missing:
                document.data[key] = value
                document.save()


if __name__ == "__main__":
    BulkReplaceTag().main()

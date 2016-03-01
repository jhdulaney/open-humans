from common.app_configs import BaseConnectionAppConfig


class IlluminaUYGConfig(BaseConnectionAppConfig):
    """
    Configure the Illuminy Understand Your Genome activity application.
    """

    name = __package__
    verbose_name = 'Illumina Understand Your Genome'

    connection_template = 'partials/upload-activity.html'

    data_description = {
        'name': 'Genome data',
        'description': (
            'Whole genome data in gVCF format. This can reveal information '
            "about health, traits, ancestry, and who you're related to."),
    }
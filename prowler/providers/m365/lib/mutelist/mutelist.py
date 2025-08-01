from prowler.lib.check.models import CheckReportM365
from prowler.lib.mutelist.mutelist import Mutelist
from prowler.lib.outputs.utils import unroll_dict, unroll_tags


class M365Mutelist(Mutelist):
    def is_finding_muted(
        self,
        finding: CheckReportM365,
        tenant_id: str,
    ) -> bool:
        return self.is_muted(
            tenant_id,
            finding.check_metadata.CheckID,
            finding.location,
            finding.resource_name,
            unroll_dict(unroll_tags(finding.resource_tags)),
        )

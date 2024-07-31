"""Module to handle all operations with application scopes"""

SCS_URI = "/scans/results"

class AquaCodeScan:
    """Class to create methods for interacting with all application scope operations"""

    def __init__(self, auth_client):
        self.auth_client = auth_client

    def get_results_summary(self):
        """function to get the result summary"""
        raw_response = self.auth_client.authenticated_get(
            resource="scs",
            endpoint=f"{SCS_URI}/summary"
        )
        return raw_response
    def get_results_by_checks(self):
        """function to get the result summary"""
        raw_response = self.auth_client.authenticated_get(
            resource="scs",
            endpoint=f"{SCS_URI}/checks"
        )
        return raw_response
    def get_results_by_files(self, options):
        """function to get the result summary"""
        raw_response = self.auth_client.authenticated_get(
            resource="scs",
            endpoint=f"{SCS_URI}/files",
            params=self.__format_results_query(options)
        )
        return raw_response
    def get_flatten_results(self, options):
        """function to get the result summary"""
        raw_response = self.auth_client.authenticated_get(
            resource="scs",
            endpoint=f"{SCS_URI}",
            params=self.__format_results_query(options)
        )
        return raw_response
    def __format_results_query(self, options, page=1, pagesize=100):
        """function to help build the params"""
        return f"""?\
                {f'avdIds={options.get("avdIds")}' if options.get("avdIds") else ""}\
                {f'&scanIds={options.get("scanIds")}' if options.get("scanIds") else ""}\
                {f'&repositoryIds={options.get("repositoryIds")}' if options.get("repositoryIds") else ""}\
                {f'&scanCategory={options.get("scanCategory")}' if options.get("scanCategory") else ""}\
                {f'&search={options.get("search")}' if options.get("search") else ""}\
                {f'&file={options.get("file")}' if options.get("file") else ""}\
                {f'&resource={options.get("resource")}' if options.get("resource") else ""}\
                {f'&vendorFix={options.get("vendorFix")}' if options.get("vendorFix") else ""}\
                {f'&repositoryName={options.get("repositoryName")}' if options.get("repositoryName") else ""}\
                {f'&packageName={options.get("packageName")}' if options.get("packageName") else ""}\
                {f'&from={options.get("from")}' if options.get("from") else ""}\
                {f'&to={options.get("to")}' if options.get("to") else ""}\
                {f'&reachable={options.get("reachable")}' if options.get("reachable") else ""}\
                {f'&direct={options.get("direct")}' if options.get("direct") else ""}\
                {f'&cwe={options.get("cwe")}' if options.get("cwe") else ""}\
                {f'&category={options.get("category")}' if options.get("category") else ""}\
                {f'&severity={options.get("severity")}' if options.get("severity")else ""}\
                {f'&organization={options.get("organization")}' if options.get("organization") else ""}\
                {f'&system={options.get("system")}' if options.get("system") else ""}\
                {f'&size={pagesize}'},
                {f'&page={page}'},
                {f'&sortKey={options.get("sortKey", "severity")}'},
                {f'&sortOrder={options.get("sortOrder", "asc")}'}"""
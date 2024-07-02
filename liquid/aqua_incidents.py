"""Module to handle all operations with incidents and suppression rules"""

INCIDENT_URI = "/v2/incidents"
SUPPRESSION_RULE_URI = f"{INCIDENT_URI}/suppression_rules"


# pylint: disable=fixme
class AquaIncidents:
    """Class to create methods for interacting with incident and suppression rules operations"""

    def __init__(self, auth_client):
        self.auth_client = auth_client

    def get_incidents(self, options, page=1, pagesize="25", skip_count="false"):
        """Get Incidents."""
        raw_incident_response = self.auth_client.authenticated_get(
            f"{INCIDENT_URI}{self.__format_incident_query(options, page, pagesize, skip_count)}"
        )
        page_options = {"page": page, "pagesize": pagesize, "skip_count": skip_count}
        result = self.__page_records(
            options,
            page_options,
            raw_incident_response.get("count"),
            raw_incident_response.get("result"),
        )
        return result

    def get_incident_totals(self, options):
        """Get summary totals of incidents given the search criteria in options"""
        raw_incident_response = self.auth_client.authenticated_get(
            f"""{INCIDENT_URI}/totals{self.__format_incident_query(
                options,
                page=1,
                pagesize=None,
                skip_count=None)}"""
        )
        return raw_incident_response

    def get_incident(self, incident_id):
        """Get a specific incident details"""
        raw_incident_response = self.auth_client.authenticated_get(
            f"{INCIDENT_URI}/{incident_id}"
        )
        return raw_incident_response

    def get_incident_timeline(self, incident_id, options):
        """gets the incident timeline for a specific incident"""
        # The options supported in timeline are:
        # search, type, interval, from_date, to_date and group_by
        raw_incident_response = self.auth_client.authenticated_get(
            f"""{INCIDENT_URI}/{incident_id}/{self.__format_incident_query(
                options,
                page=1,
                pagesize="200",
                skip_count=None)}"""
        )
        page_options = {"page": 1, "pagesize": "200", "skip_count": None}
        result = self.__page_records(
            options,
            page_options,
            record_count=raw_incident_response.get("count"),
            result=raw_incident_response.get("result"),
        )
        return result

    def get_suppression_rule(self, rule_id):
        """Get a specific suppression rule details"""
        raw_response = self.auth_client.authenticated_get(
            f"{SUPPRESSION_RULE_URI}/{rule_id}"
        )
        return raw_response

    def delete_suppression_rule(self, rule_id):
        """Deletes a specific suppression rule"""
        raw_response = self.auth_client.authenticated_delete(
            f"{SUPPRESSION_RULE_URI}/{rule_id}"
        )
        return raw_response.status_code == 200

    def list_suppression_rules(self, options):
        """List all suppression rules"""
        # The options supported in list are search, enabled and order_by
        raw_response = self.auth_client.authenticated_get(
            f"{SUPPRESSION_RULE_URI}/list"
        )
        page_options = {"page": 1, "pagesize": "200", "skip_count": None}
        result = self.__page_records(
            options,
            page_options,
            record_count=raw_response.get("count"),
            result=raw_response.get("result"),
        )
        return result

    def insert_suppression_rule(self, rule):
        """Insert a suppression rule"""
        raw_response = self.auth_client.authenticated_put(
            f"{SUPPRESSION_RULE_URI}/insert", data=rule
        )
        return raw_response.status_code == 200

    def update_suppression_rule(self, rule):
        """Update a suppression rule"""
        raw_response = self.auth_client.authenticated_put(
            f"{SUPPRESSION_RULE_URI}/update", data=rule
        )
        return raw_response.status_code == 200

    def __page_records(self, options, page_options, record_count, result):
        page = page_options.get("page")
        pagesize = page_options.get("pagesize")
        skip_count = page_options.get("skip_count")
        if result:
            while len(result) < record_count:
                page += 1
                raw_response = self.auth_client.authenticated_get(
                    INCIDENT_URI
                    + {
                        self.__format_incident_query(
                            options, page, pagesize, skip_count
                        )
                    }
                )
                # TODO Catch for non 200 response
                if raw_response.get("result"):
                    result.extend(raw_response.get("result"))
                else:
                    break
        return result

    def __format_incident_query(self, options, page, pagesize, skip_count):
        return f"""?\
                search={options.get("search") if options.get("search") else ""}\
                {f'&interval={options.get("interval")}' if options.get("interval") else ""}\
                {f'&from_date={options.get("from_date")}' if options.get("from_date") else ""}\
                {f'&to_date={options.get("to_date")}' if options.get("to_date") else ""}\
                {f'&host_group={options.get("host_group")}' if options.get("host_group") else ""}\
                {f'&cluster={options.get("cluster")}' if options.get("cluster") else ""}\
                {f'&severity={options.get("severity")}' if options.get("severity") else ""}\
                {f'&order_by={options.get("order_by")}' if options.get("order_by") else ""}\
                {f'&group_by={options.get("group_by")}' if options.get("group_by") else ""}\
                {f'&container_id={options.get("container_id")}'
                 if options.get("container_id") else ""}\
                {f'&container_name={options.get("container_name")}'
                 if options.get("container_name") else ""}\
                {f'&host_id={options.get("host_id")}' if options.get("host_id") else ""}\
                {f'&host_name={options.get("host_name")}' if options.get("host_name") else ""}\
                {f'&result={options.get("result")}' if options.get("result") else ""}\
                {f'&main_categories={options.get("main_categories")}'
                 if options.get("main_categories") else ""}\
                {f'&page={page}' if page else ""}\
                {f'&page={pagesize}' if pagesize else ""}\
                {f'&page={skip_count}' if skip_count else ""}"""

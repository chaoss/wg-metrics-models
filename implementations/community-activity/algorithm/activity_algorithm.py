import math

COMMIT_FREQUENCY_WEIGHT_ACTIVITY = 0.18009
UPDATED_SINCE_WEIGHT_ACTIVITY = -0.12742
MAINTAINER_COUT_ACTIVITY = 0.2090
CODE_REVIEW_COUNT_WEIGHT_ACTIVITY = 0.04919
CLOSED_ISSUES_WEIGHT_ACTIVITY = 0.04919
UPDATED_ISSUES_WEIGHT_ACTIVITY = 0.04919
COMMENT_FREQUENCY_WEIGHT_ACTIVITY = 0.07768
CONTRIBUTOR_COUNT_WEIGHT_ACTIVITY = 0.18009
ORG_COUNT_WEIGHT_ACTIVITY = 0.11501
RECENT_RELEASES_WEIGHT_ACTIVITY = 0.03177
CREATED_SINCE_WEIGHT_ACTIVITY = 0.07768
MEETING_ACTIVITY = 0.02090
MEETING_ATTENDEE_COUNT_ACTIVITY = 0.02090

# Max thresholds for various parameters.
CODE_REVIEW_COUNT_THRESHOLD_ACTIVITY = 15
CREATED_SINCE_THRESHOLD_ACTIVITY = 120
UPDATED_SINCE_THRESHOLD_ACTIVITY = 12
CONTRIBUTOR_COUNT_THRESHOLD_ACTIVITY = 1000
ORG_COUNT_THRESHOLD_ACTIVITY = 10
COMMIT_FREQUENCY_THRESHOLD_ACTIVITY = 1000
RECENT_RELEASES_THRESHOLD_ACTIVITY = 26
CLOSED_ISSUES_THRESHOLD_ACTIVITY = 1000
UPDATED_ISSUES_THRESHOLD_ACTIVITY = 1000
COMMENT_FREQUENCY_THRESHOLD_ACTIVITY = 15
DEPENDENTS_COUNT_THRESHOLD_ACTIVITY = 500000


# Others.
TOP_CONTRIBUTOR_COUNT = 15
ISSUE_LOOKBACK_DAYS = 90
RELEASE_LOOKBACK_DAYS = 365
FAIL_RETRIES = 7

def get_param_score(param, max_value, weight=1):
    """Return paramater score given its current value, max value and
    parameter weight."""
    return (math.log(1 + param) / math.log(1 + max(param, max_value))) * weight

def community_activity_score(item): 
    total_weight_ACTIVITY  = ( CREATED_SINCE_WEIGHT_ACTIVITY + UPDATED_SINCE_WEIGHT_ACTIVITY +
                            CONTRIBUTOR_COUNT_WEIGHT_ACTIVITY + 
                            COMMIT_FREQUENCY_WEIGHT_ACTIVITY + 
                            CLOSED_ISSUES_WEIGHT_ACTIVITY + UPDATED_ISSUES_WEIGHT_ACTIVITY +
                            COMMENT_FREQUENCY_WEIGHT_ACTIVITY )
    criticality_score = round(  
                        ((get_param_score(item["created_since"],
                                        CREATED_SINCE_THRESHOLD_ACTIVITY, CREATED_SINCE_WEIGHT_ACTIVITY)) +
                        (get_param_score(item["updated_since"],
                                        UPDATED_SINCE_THRESHOLD_ACTIVITY, UPDATED_SINCE_WEIGHT_ACTIVITY)) +
                        (get_param_score(item["contributor_count"],
                                        CONTRIBUTOR_COUNT_THRESHOLD_ACTIVITY,
                                        CONTRIBUTOR_COUNT_WEIGHT_ACTIVITY)) +                   
                        (get_param_score(item["commit_frequency"],
                                        COMMIT_FREQUENCY_THRESHOLD_ACTIVITY,
                                        COMMIT_FREQUENCY_WEIGHT_ACTIVITY)) +                
                        (get_param_score(item["closed_issue_count"],
                                        CLOSED_ISSUES_THRESHOLD_ACTIVITY, CLOSED_ISSUES_WEIGHT_ACTIVITY)) +
                        (get_param_score(item["updated_issues_count"],
                                        UPDATED_ISSUES_THRESHOLD_ACTIVITY, UPDATED_ISSUES_WEIGHT_ACTIVITY))+
                        (get_param_score(item["comment_frequency"],
                                        COMMENT_FREQUENCY_THRESHOLD_ACTIVITY, COMMENT_FREQUENCY_WEIGHT_ACTIVITY))) /
                        total_weight_ACTIVITY, 5)
    return criticality_score

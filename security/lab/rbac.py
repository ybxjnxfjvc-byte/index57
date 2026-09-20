PERMISSIONS={
 'visitor':{'view_public'},
 'learner':{'view_public','submit_own_result','view_own_result'},
 'reviewer':{'view_public','view_anonymized_results'},
 'admin':{'view_public','view_anonymized_results','manage_demo_config'},
}
def allowed(role, action, *, owner=False):
 if role not in PERMISSIONS:return False
 if action in {'submit_own_result','view_own_result'} and not owner:return False
 return action in PERMISSIONS[role]

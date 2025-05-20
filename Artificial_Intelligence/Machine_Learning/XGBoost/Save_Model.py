import json
import joblib

best_params = grid_search_xgb.best_params_

with open('best_params.json', 'w') as f:
    json.dump(best_params, f)

# Optionally save the entire GridSearchCV object
joblib.dump(grid_search_xgb, 'grid_search_result.pkl')

# Load parameters
with open('best_params.json', 'r') as f:
    loaded_params = json.load(f)

# Load full model
loaded_model = joblib.load('grid_search_result.pkl') 

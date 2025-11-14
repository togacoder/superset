PYTHONPATH = '/app/pythonpath'
SECRET_KEY = 'J8mMJu7b/K10sAeoXycsd3lgcZ2XkFp4s9q0PZSH3wriUakNdCLC0luL'
SQLALCHEMY_DATABASE_URI = 'mysql://superset:superset1234@mysql/superset'
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
}
CONTENT_SECURITY_POLICY_WARNING = False
#TALISMAN_ENABLED = False
TALISMAN_CONFIG = { 
     "content_security_policy": { 
         "base-uri": ["'self'"], 
         "default-src": ["'self'"], 
         "img-src": [ 
             "'self'", 
             "blob:", 
             "data:", 
             "https://apachesuperset.gateway.scarf.sh", 
             "https://static.scarf.sh/", 
             # "https://cdn.brandfolder.io", # Uncomment when SLACK_ENABLE_AVATARS is True       # noqa: E501 
             "ows.terrestris.de", 
             "https://cdn.document360.io", 
             "https://jam-capture-unisonleague.ateamid.com/",
         ], 
         "worker-src": ["'self'", "blob:"], 
         "connect-src": [ 
             "'self'", 
             "https://api.mapbox.com", 
             "https://events.mapbox.com", 
             "https://tile.openstreetmap.org", 
             "https://tile.osm.ch", 
         ], 
         "object-src": "'none'", 
         "style-src": [ 
             "'self'", 
             "'unsafe-inline'", 
         ], 
         "script-src": ["'self'", "'strict-dynamic'"], 
     }, 
     "content_security_policy_nonce_in": ["script-src"], 
     "force_https": False, 
     "session_cookie_secure": False, 
 }
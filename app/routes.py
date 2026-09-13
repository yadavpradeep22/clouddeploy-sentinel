from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "CloudDeploy Sentinel"
    })


@api.get("/version")
def version():
    return jsonify({
        "application": "CloudDeploy Sentinel",
        "version": "1.0.0"
    })

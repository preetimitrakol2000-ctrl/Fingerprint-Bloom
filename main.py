from anomaly_detector import standardize_hw_string
from bloom_core import ProbabilisticFilter

if __name__ == "__main__":
    print("🔒 Initializing Fingerprint-Bloom Security Network Core...")

    firewall = ProbabilisticFilter(size=128)
    
    # Authenticate safe baseline device signatures
    firewall.insert_signature(standardize_hw_string("Thermostat_Node_01"))
    firewall.insert_signature(standardize_hw_string("Gateway_Server_Main"))

    # Test incoming connections
    device_a = "Thermostat_Node_01"
    device_b = "Unknown_Attack_Hardware"

    verdict_a = firewall.check_existence(standardize_hw_string(device_a))
    verdict_b = firewall.check_existence(standardize_hw_string(device_b))

    print(f"\n📡 Scanning Inbound Handshake Packet: Identifier -> \"{device_a}\"")
    print(f"   🔮 Firewall Lookup Verdict: {'✅ TRUSTED NODE MATCH' if verdict_a else '🚨 MALICIOUS THREAT DETECTED'}")

    print(f"\n📡 Scanning Inbound Handshake Packet: Identifier -> \"{device_b}\"")
    print(f"   🔮 Firewall Lookup Verdict: {'✅ TRUSTED NODE MATCH' if verdict_b else '🚨 MALICIOUS THREAT DETECTED (REJECT SIGNAL)'}")

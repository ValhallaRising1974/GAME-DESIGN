
// Valhalla Rising - The Parchment
// World Builder - Base Structure

using UnityEngine;

public class ParchmentWorldBuilder : MonoBehaviour
{
    [Header("Main Routes")]
    public Route highland;
    public Route middleway;
    public Route firestarter;

    [Header("Bases")]
    public BaseStructure leftBase;
    public BaseStructure rightBase;

    [Header("Jungle Zones")]
    public JungleZone gnomeSanctuary;
    public JungleZone goblinRefuge;
    public JungleZone nymphGarden;
    public JungleZone ransorDomain;

    [Header("Obelisks")]
    public Obelisk[] highlandObelisks;
    public Obelisk[] middlewayObelisks;
    public Obelisk[] firestarterObelisks;

    [Header("Sky and Atmosphere")]
    public SkySettings skySettings;

    void Start()
    {
        // Initialize Map
        BuildMap();
    }

    void BuildMap()
    {
        // Here we will programmatically create routes, bases, jungles and obelisks
        Debug.Log("Valhalla Rising - Map Initialized!");
    }
}

[System.Serializable]
public class Route
{
    public string name;
    public float length;
    public string terrainType;
    public string obstacleDetails;
    public string champions;
}

[System.Serializable]
public class BaseStructure
{
    public string owner;
    public string buildingStyle;
    public string groundMaterial;
    public string magicalProtection;
}

[System.Serializable]
public class JungleZone
{
    public string zoneName;
    public string locationDetails;
    public string combatStyle;
    public string terrainType;
}

[System.Serializable]
public class Obelisk
{
    public float height;
    public float durability;
    public string location;
}

[System.Serializable]
public class SkySettings
{
    public bool dayNightCycle;
    public float cycleDurationMinutes;
    public string[] cosmicEffects;
}

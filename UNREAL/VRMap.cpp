// Valhalla Rising – The Parchment
// VRMap.cpp

#include "VRMap.h"

AVRMap::AVRMap()
{
    PrimaryActorTick.bCanEverTick = true;
}

void AVRMap::BeginPlay()
{
    Super::BeginPlay();
    UE_LOG(LogTemp, Warning, TEXT("Valhalla Map Initialized: Highland, Midleway, Firestarter, Oblivion, Obelisks ready"));
}

void AVRMap::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
    // Placeholder for dynamic obelisk interactions or map logic
}
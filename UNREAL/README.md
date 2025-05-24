// Valhalla Rising – The Parchment
// VRMap.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "VRMap.generated.h"

UCLASS()
class VALHALLARISING_API AVRMap : public AActor
{
    GENERATED_BODY()
    
public:    
    AVRMap();

protected:
    virtual void BeginPlay() override;

public:    
    virtual void Tick(float DeltaTime) override;

    // Routes
    UPROPERTY(EditAnywhere, Category = "Map Layout")
    AActor* Highland;       // Top Lane

    UPROPERTY(EditAnywhere, Category = "Map Layout")
    AActor* Midleway;       // Middle Lane

    UPROPERTY(EditAnywhere, Category = "Map Layout")
    AActor* Firestarter;    // Bottom Lane

    UPROPERTY(EditAnywhere, Category = "Map Layout")
    AActor* Oblivion;       // Jungle

    // Bases
    UPROPERTY(EditAnywhere, Category = "Points of Interest")
    AActor* TeamBase_Light;

    UPROPERTY(EditAnywhere, Category = "Points of Interest")
    AActor* TeamBase_Shadow;

    // Central Altar
    UPROPERTY(EditAnywhere, Category = "Points of Interest")
    AActor* AltarOfEssence;
};

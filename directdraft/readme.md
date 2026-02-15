Result: 
With humanoid base
https://github.com/BoQsc/godot-demo-projects/tree/quaternius-ragdoll-walkthrough/3d/ragdoll_physics/characters_quaternius

![2026-02-15 12-27-24|video](upload://eJnw6lZIejiOkFxPabSOlJlL4Zx.mp4)

With Human base and Idle animation pose enabled. (Humanoid base as donor of PhysicalSkeleton)
https://github.com/BoQsc/godot-demo-projects/tree/quanternius-ragdoll-walkthrough-human-base/3d/ragdoll_physics/characters_quaternius

![2026-02-15 15-44-13|video](upload://sBydFdNXjKSS8pwTJBpquEeq1eX.mp4)
### Preparation
Asset (CC0):
https://quaternius.itch.io/universal-animation-library  
Testing Playground and Godot Ragdoll Reference:

https://github.com/godotengine/godot-demo-projects/tree/master/3d/ragdoll_physics   
### Start 
1. Let's start by opening the `godot-demo-projects\3d\ragdoll_physics\` project.2. 
3. Create folder `characters_quaternius` in the project folder.
   * Copy the `AnimationLibrary_Godot_Standard.glb` into this folder.
   * Create a new Node 3D Scene `quaternius_ragdoll.tscn` and drag this `.glb` file into the scene. 
3. Let's retarget the model's skeleton to create a GeneralSkeleton. 
This will allow for easier transfer of PhysicalSkeleton later on.

![image|690x388](upload://jbyRHr9niFVgC8gqtNYlwnENLv0.jpeg)


4. Let's mark the model as Editable Children

![image|690x388](upload://5Jpa4aqFmI4KwYAIN5FVKiqPp9Z.jpeg)

5. Let's create a Physical Skeleton.

![image|690x388](upload://bHUNzvKeSDTpxVaZMKiRdoBArTk.jpeg)

6. Let's inspect the newly created **PhysicalBoneSimulator3D** by entering **display overdraw**.

![image|690x388](upload://gwc8o9OvyFaya7A7erGihIvdtSi.png)

7. Let's inspect the first Physical bone of the PhysicalBoneSimulator3D: `Physical Bone root`.
  This is clearly some kind of helper bone, so we are immediately deleting it. (it's obstructing the physical bones of legs)

![image|690x388](upload://qDFzpvrcpCvyn329jNMyOdBXbwH.jpeg)

8. Now that we have no more weird bones, let's continue by enlarging the physical bones by clicking on CollisionShape3D and uniformly scaling them using **scaling handles**.

**Tip:** I generally have personal belief that **rotation and positioning** should be done on the **entire PhysicalBone** and **scaling** should be done by scaling the **CollisionShape3D of the Physical Bone**.

It took me around 11 minutes to complete scaling and rotating the bones and I still believe it's far from perfect due to my limited knowledge as of now.

Full Video: https://github.com/BoQsc/quaternius-ragdoll-walkthrough/releases/download/0/2026-02-14.21-20-11.-.Copy.mp4


![image|690x388](upload://4XjuPI5ZmypzgltKtW0A9lCCrd6.jpeg)



9. Now that we have bones matching or outmatching the mesh of the model, let's point out the obvious now: where is the head bone? I don't know. We will figure it out along the way if anything can be done about it. in the worst case scenario we would just  scale up the neck physical bone to accomodate for the head. However I maybe already figured out how to bring up head physical bone.

![image|690x388](upload://uVZOZ4NGGBb9gJ55jUYB0nADK1y.jpeg)


### Creating Missing Head Physical Bone
We simply duplicate the neck physical bone and select Bone name Head then adjust the head physical bone location and size the CollisionShape3D so it fits the mesh of the head.

![image|690x388](upload://rtaLGsNuOHfnAHB371u6F3CakAg.jpeg)

Remember to make the CollisionShape3D of the Head a Unique element:

![image|690x388](upload://rdWOBQO96arTuaFov49BTsQxVXE.jpeg)

And so after some scaling adjustments to the CollisionShape3D and transform adjustments of PhysicalBone itself we have a head PhysicalBone.

![image|690x388](upload://7msiaFdAJz4gVFrWbIYhov4Ax6X.jpeg)

10. Let's collapse the PhysicalBoneSimulator  node so we can easily select subnodes

![image|690x388](upload://67MJxPWI6ABh3J8ZFvAAsbjGHG0.jpeg)


11. Let's now change all bones joint types to cone join type.

![image|690x388](upload://jRktGJgnmfMki8PJKqkTUqf6fVA.jpeg)


12. Let's apply the joint constraints to all the joints.
     * joint_constraints/swing_span: 20.0
     * joint_constraints/twist_span: 20.0


![image|690x388](upload://36t5qnOgppmbe0WUNzOQCtX0C2C.jpeg)

13. Let's apply friction and bounciness to all the bones.

     * friction: 0.8
     * bouncines: 0.6

![image|690x388](upload://utVZnyh4pGErMTU913asQhaUmMB.jpeg)

14. Now that we have all this setup we can go on and introduce this ragdoll into the demo.
15. Let's copy the `mannequiny_ragdoll.gd` script into our folder `characters_quaternius`

![image|690x388](upload://5qk7JA1ieUajfudRX6Aca7O1ZiR.jpeg)

16.  Let's edit our  `mannequiny_ragdoll.gd` by replacing/changing nodes paths in the script.

![image|690x388](upload://y82Z5Rcw9a7HcBXL2QcfXmdSgQ5.png)

17. Let's attach our `mannequiny_ragdoll.gd` to our top level Node 3D

![image|690x388](upload://ypTh3sWecJOKVIRxwj3Qjp1RupY.png)

18. Let's copy the `AudioStreamPlayers` from the `mannequiny_ragdoll.tscn` 

![image|690x388](upload://6GqvY8s2B91unspxPFM65rYEd81.png)
19. Paste the `AudioStreamPlayers` to our QunaterniusRagdoll scene.

![image|690x388](upload://diFjnYo4Br9TdKwfpVnW4jOoyz1.png)


20. Let's edit the `ragdoll_physics.gd` so that pressing spacebar would spawn our ragdoll.

![image|690x388](upload://kjtw8I0ilZQT3CGNOQp0d0jf2aG.png)

21. Let's run the `ragdoll_physics.tscn` scene. 
  As we can see our ragdoll might not be perfect, 
looking for your suggestions on how to make it more perfect.

![2026-02-15 12-27-24|video](upload://eJnw6lZIejiOkFxPabSOlJlL4Zx.mp4)


### Transfer PhysicalSkeleton/Ragdoll to Quaternius Human Base
To transfer the PhysicalSkeleton you have to **duplicate it and then move it**, instead of just moving or copying it.

1. First, let's download [Quaternius Universal Base Characters](https://quaternius.com/packs/universalbasecharacters.html)
2. Let's do Skeleton3D retargeting and do reimport of our **Superhero_Male_FullBody.gltf**

![image|690x388](upload://qEvLvjNP84QKpgVBXJeaz4FrGuM.jpeg)

3. Let's add **Superhero_Male_FullBody.gltf** into the scene.

![image|690x388](upload://w9LdU8WW9a0NhuRXU2xNylcTRyD.jpeg)

4. Let's mark it as Editable Children

![image|690x388](upload://cNJ6qvfzJfzOO6dHM0ILRZeIBSN.jpeg)

5. Let's duplicate the PhysicalBoneSimulator3D

![image|690x388](upload://wvQOrMMePh4cue9TholrrYKrQ7Z.jpeg)

6. Let's move the duplicated `PhysicalBoneSimulator3D2` to the human base.

![image|690x388](upload://7foxdz0K2XKb0GV64gBqgcgwbv8.jpeg)

7. Let's rename `PhysicalBoneSimulator3D2` to `PhysicalBoneSimulator3D`

![image|690x388](upload://lHl4m18cLWdrC0kTY7vyRsKrzVI.jpeg)

8. Done. We successfully transfered the PhysicalSkeleton to the Human base.
9. Let's delete the donor humanoid  base (`AnimationLibrary_Godot_Standard`)

![image|690x388](upload://7pqvrWGtE6JUpiskpQK0szT0rqt.jpeg)

10. Let's reintroduce the Human Base into Godot playground.

![image|690x388](upload://tvNHpb1UMcj8CarzBmPM9Luse8K.png)

11. Let's see what we have.
![2026-02-15 15-28-51|video](upload://kf5mfTsxoAUcpoBE5yMPXudBACi.mp4)

12. Let's apply idle pose from previous animation library. 
13. First let's mark and reimport `AnimationLibrary_Godot_Standard.glb` as animation library.

![image|690x388](upload://sLwW3rTd8iqD3lD0nCFdqnSQJsN.jpeg)

14.  Retarget Skeleton3D of Animation Library 
   ( We already retargeted animation library skeleton)
![image|690x388](upload://Yg5pAfrMqpBklIGvOuVE1rjNNJ.jpeg)

14. Add new animation player to the human base.
![image|690x388](upload://gE4RhyPuQinWtmEoetT612B4n9H.jpeg)

15. Load up animation library.

![image|690x388](upload://5ZcHahrjQXpEuP6Lu64UuCmsKlp.jpeg)
![image|690x388](upload://oTyFUp5oxBr6QQe2wZt26oEjIAC.jpeg)
![image|690x388](upload://aBtFrDYOe74KoW5Fc7F8re0S77O.png)
![image|690x388](upload://A0HLFQC9Hzty1G2Xngn9B52dQH1.jpeg)


16 Select the Idle animation and start the  `ragdoll_physics.tscn` ragdolls scene.

![image|690x388](upload://hH7UvcFALJ4Tib1Y5HjqZDGAqwn.jpeg)

![2026-02-15 15-44-13|video](upload://sBydFdNXjKSS8pwTJBpquEeq1eX.mp4)

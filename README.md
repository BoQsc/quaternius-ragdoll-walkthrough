Result: 
With humanoid base
https://github.com/BoQsc/godot-demo-projects/tree/quaternius-ragdoll-walkthrough/3d/ragdoll_physics/characters_quaternius

![2026-02-15 12-27-24|video](media/673fa2acf23870bd1d99a7272e0991cfd71eca6f.mp4)

With Human base and Idle animation pose enabled. (Humanoid base as donor of PhysicalSkeleton)
https://github.com/BoQsc/godot-demo-projects/tree/quanternius-ragdoll-walkthrough-human-base/3d/ragdoll_physics/characters_quaternius

![2026-02-15 15-44-13|video](media/c87b8f6344ead03c79265d4f27a299e4b17ef133.mp4)
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

![image|690x388](media/8677e676b7cc3c5e1630dff561c7487b5166f1d6.jpeg)


4. Let's mark the model as Editable Children

![image|690x388](media/282cd65be0a0919ad7b7bb7203682850de194a97.jpeg)

5. Let's create a Physical Skeleton.

![image|690x388](media/520ec5684931cc1f0e38884b98bfe194f0b7bbc2.jpeg)

6. Let's inspect the newly created **PhysicalBoneSimulator3D** by entering **display overdraw**.

![image|690x388](media/73c6790f9cc9129b1a56adec2cefa5cae3963ae2.png)

7. Let's inspect the first Physical bone of the PhysicalBoneSimulator3D: `Physical Bone root`.
  This is clearly some kind of helper bone, so we are immediately deleting it. (it's obstructing the physical bones of legs)

![image|690x388](media/bab4850a488aa533636bc914edf50637f1f6a66f.jpeg)

8. Now that we have no more weird bones, let's continue by enlarging the physical bones by clicking on CollisionShape3D and uniformly scaling them using **scaling handles**.

**Tip:** I generally have personal belief that **rotation and positioning** should be done on the **entire PhysicalBone** and **scaling** should be done by scaling the **CollisionShape3D of the Physical Bone**.

It took me around 11 minutes to complete scaling and rotating the bones and I still believe it's far from perfect due to my limited knowledge as of now.

Full Video: https://github.com/BoQsc/quaternius-ragdoll-walkthrough/releases/download/0/2026-02-14.21-20-11.-.Copy.mp4


![image|690x388](media/22bd27c0bae9576b7e4bd1afdfcdb1a85a05fd68.jpeg)



9. Now that we have bones matching or outmatching the mesh of the model, let's point out the obvious now: where is the head bone? I don't know. We will figure it out along the way if anything can be done about it. in the worst case scenario we would just  scale up the neck physical bone to accomodate for the head. However I maybe already figured out how to bring up head physical bone.

![image|690x388](media/d8cf8e948e299a4ea59bfef15d6fe2a02e1b6fc0.jpeg)


### Creating Missing Head Physical Bone
We simply duplicate the neck physical bone and select Bone name Head then adjust the head physical bone location and size the CollisionShape3D so it fits the mesh of the head.

![image|690x388](media/c086ef1b5818adc30547dfaa72e7ac93a9366808.jpeg)

Remember to make the CollisionShape3D of the Head a Unique element:

![image|690x388](media/bece58e46e08cc7885c5b528b3136b75e1fbe04e.jpeg)

And so after some scaling adjustments to the CollisionShape3D and transform adjustments of PhysicalBone itself we have a head PhysicalBone.

![image|690x388](media/339910dc8d6c039986f7a449e754eba9913021f3.jpeg)

10. Let's collapse the PhysicalBoneSimulator  node so we can easily select subnodes

![image|690x388](media/2aee5bca4e82823ed2b540162573e931c9160758.jpeg)


11. Let's now change all bones joint types to cone join type.

![image|690x388](media/8b3097dc67bc07e1b971b4afdd615c18dc51b12e.jpeg)


12. Let's apply the joint constraints to all the joints.
     * joint_constraints/swing_span: 20.0
     * joint_constraints/twist_span: 20.0


![image|690x388](media/15c1ba677f26deb288f815ccbb724637b43406ca.jpeg)

13. Let's apply friction and bounciness to all the bones.

     * friction: 0.8
     * bouncines: 0.6

![image|690x388](media/d5a37f00d488aa203f96e9fe350bec1881881ddd.jpeg)

14. Now that we have all this setup we can go on and introduce this ragdoll into the demo.
15. Let's copy the `mannequiny_ragdoll.gd` script into our folder `characters_quaternius`

![image|690x388](media/2604a89651fd7f50e66d3aa17cd457ae54b1c23d.jpeg)

16.  Let's edit our  `mannequiny_ragdoll.gd` by replacing/changing nodes paths in the script.

![image|690x388](media/ef32d08f1b735bcd73d796722b0e3b7378d8767d.png)

17. Let's attach our `mannequiny_ragdoll.gd` to our top level Node 3D

![image|690x388](media/f1372bf152805f0907fc35d53eebe0b36cc82eca.png)

18. Let's copy the `AudioStreamPlayers` from the `mannequiny_ragdoll.tscn` 

![image|690x388](media/2ed8d3fc94bf863a3338bd3270a3674dc1edd885.png)
19. Paste the `AudioStreamPlayers` to our QunaterniusRagdoll scene.

![image|690x388](media/5d386ef14e1ec0983dcbc9e32e07a01fca499003.png)


20. Let's edit the `ragdoll_physics.gd` so that pressing spacebar would spawn our ragdoll.

![image|690x388](media/8e5f15a1776967c4700791a2cb6df4eaee083a96.png)

21. Let's run the `ragdoll_physics.tscn` scene. 
  As we can see our ragdoll might not be perfect, 
looking for your suggestions on how to make it more perfect.

![2026-02-15 12-27-24|video](media/673fa2acf23870bd1d99a7272e0991cfd71eca6f.mp4)


### Transfer PhysicalSkeleton/Ragdoll to Quaternius Human Base
To transfer the PhysicalSkeleton you have to **duplicate it and then move it**, instead of just moving or copying it.

1. First, let's download [Quaternius Universal Base Characters](https://quaternius.com/packs/universalbasecharacters.html)
2. Let's do Skeleton3D retargeting and do reimport of our **Superhero_Male_FullBody.gltf**

![image|690x388](media/bacce1ada2187b04782311ae0beb769335579414.jpeg)

3. Let's add **Superhero_Male_FullBody.gltf** into the scene.

![image|690x388](media/e1600daac1c52ee40cbe7464b2092d4b6b275e9f.jpeg)

4. Let's mark it as Editable Children

![image|690x388](media/59b91da5e356dd4b859b87926ed14ec1a9db4279.jpeg)

5. Let's duplicate the PhysicalBoneSimulator3D

![image|690x388](media/e3df4df9efedf99f8eedaac342b74f306214f487.jpeg)

6. Let's move the duplicated `PhysicalBoneSimulator3D2` to the human base.

![image|690x388](media/32ccbe7ef76ada05ed92f30a69c51d72d5cb8736.jpeg)

7. Let's rename `PhysicalBoneSimulator3D2` to `PhysicalBoneSimulator3D`

![image|690x388](media/9813d592f94889c8b98ac058921cd424eafd404e.jpeg)

8. Done. We successfully transfered the PhysicalSkeleton to the Human base.
9. Let's delete the donor humanoid  base (`AnimationLibrary_Godot_Standard`)

![image|690x388](media/33ef0c15b4ce2a41d68727389653e1380cd52fe5.jpeg)

10. Let's reintroduce the Human Base into Godot playground.

![image|690x388](media/ced75455d25a8225542538a4f40ec1ae179c8cb6.png)

11. Let's see what we have.
![2026-02-15 15-28-51|video](media/8de00e14fd8890d3d84b13c4004bee3298b425fe.mp4)

12. Let's apply idle pose from previous animation library. 
13. First let's mark and reimport `AnimationLibrary_Godot_Standard.glb` as animation library.

![image|690x388](media/c99c57fc60618926b52ff1660e6c10db34437a8d.jpeg)

14.  Retarget Skeleton3D of Animation Library 
   ( We already retargeted animation library skeleton)
![image|690x388](media/06cfce5b6a9b9954a21c1be41a72682effd22547.jpeg)

14. Add new animation player to the human base.
![image|690x388](media/74aa954d0c24a8f49062327e6e41948095e28be5.jpeg)

15. Load up animation library.

![image|690x388](media/29f6080c9e7328ef7c01c0baaeca5f25666e9327.jpeg)
![image|690x388](media/ae7bf7512521094e970725eddd0fb820106dc8f6.jpeg)
![image|690x388](media/4a524dd7e67d7b875bdcbc56830fff9f84362750.png)
![image|690x388](media/fc62b11fabc5a5e474bff560cb18200e5d795113.jpeg)


16 Select the Idle animation and start the  `ragdoll_physics.tscn` ragdolls scene.

![image|690x388](media/7c04ff1c55afde5618bec9475c08c4c3f049861f.jpeg)

![2026-02-15 15-44-13|video](media/c87b8f6344ead03c79265d4f27a299e4b17ef133.mp4)

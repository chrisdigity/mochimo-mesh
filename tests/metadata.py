import requests
import json

def test_construction_preprocess_and_metadata():
    # Define the API base URL
    base_url = "http://localhost:8080"  # Replace with your actual server address

    # Define the preprocess request payload
    preprocess_payload = {
        "network_identifier": {
            "blockchain": "mochimo",
            "network": "mainnet"
        },
        "operations": [
                    {
                        "operation_identifier": {
                            "index": 0
                        },
                        "type": "TRANSFER",
                        "status": "SUCCESS",
                        "account": {
                            "address": "0x0132d08e9796fe0e2834c067",
                            "metadata": {
                                "full_address": "0x3d40a0e3d50aa4c7ac446c30ce6c7e7ab606039557aefee42f27b1a831e3398f33166b5cfb2c7a2196f525ef8cae72d9ada0f5d3b6e3db4c321989f8ebb373217c24c8a67e33f265bd64d3664e11881579a137cc1f0f188605c42d111bedb58d9394fe89f8577d3ffa97387fe7ac08087e7bca055f69b2a16482d572a3fc7b2435c08aaf3aa1f112f5a60d05c3133f0bf9cf755b98aed6b8b0efb27b6a2a3446e44417aa0e4cbc51128a30276bf9bee9f1e50db2fa4f672b5f02a30a012fb35b57b1707eff6102f006d9093a2738659c06c58d2490f662cd149a64ec4883da0478b1172e6fbc546bfaf6b299b747c6acc0ad4d0ca4f974be7b18469a2c841264efc0b0c2ee986e259689e52122358a3318bf2dcc119fade4eaf68e6ff62e9bfcda1f5dfbc6b1946811f8eaf83c1afc1cd8a766ad72cae02f9de9301c36836b2c461137d19695ac73ba274212206b89b6ec8415ae58a214b2dff3bed3ffeff063f47dbe971d040a619df49ecccad543a4ad4b77f15faf75cab3923482e51fcc40b24f1388e4bea8e1cf4e8a24ad8f88a4c54235235626df4f91b25b5af40cd2716c0d424d730cf0ee9c0f95016f2c94c4b28dc7ae2c66a5507c48b32330edb6f1100196e5fa102c474735613834f553b5cfa8a74a18cf855a5c6787f8560d591df78941dd993c7ad8acd92be03e564747a6ef8562e7d7e46efbebeb1ce5d45c2d109dfcfc4011193b5363944106e1f059a371260a1f513e96e89ba269de5be10281da96715213709819bfb7926bc9adacea043e5832c61d86e1fd192bbbf165f202e67097a12961af977cd27d4f3a9b855212e4cf06501118ebc254a9bb76d8865e9e0feb21a4566a765c8835dd74946d6b69c7a0b97f70ac6edd152c67e6c44399a1e2fc22dddbe6dd24d5050085c11949f663c193af7031a4b130c680cf54f7ac6888e6ca7e6731cedcb069df45457fefd4adb323afdc87a6bd9919c9877382298752d9bd67d558af563737315f21ebd9f0783fc7e12555b21eef3f46edc54be1cfb7fed6a6d1e1c368d7a7b8e6552dee1ed86f7c8d2cff9b87254d6c46d1f362cde84aed2257252af35f1b64ba9212977d38c5eae8fef1094b713b9a55fe351dd44217293f95a53dd2710d7e7fc7df40564ee85c827e5fbc3212b187a988b0b1865891a953f1fb4243063cb56b2f5f8b0160cc65e07f2d6a37be225aa27c4b6f0ce2920e6cf003197f49cc93fccd958c6d6985fa1550381d282a7fa58459289f710150fb4cff79f66b44681db546ae352f40e9c90ce8ec141a4c7ff3bbd89dec632bb687a9f8adfc24ef273c2da7565134211195547eb05828c8fde2730d8599b25ad0d3c12565d747df529e800644e7d0b4ff0cd1b48f23598028e76513453ed0f0447390d8f6f35e0aaee9cff86a6c83c9cb7d100153ebc9431e921d222f29489451203d4a06585ce7a2ab34a7ac2380dfb4ca27e030e0f2459848af67787f47c8af814713c8c0ea9dd761abbca4b8bcb8af3f00a82298d4e2fbd88957f153953fd96305d0d92d2b4a8afbd0d0f49556f2b9da1fa207d1ee2a26839f14e8a81041594d1a5b675ea64588502ee0e78ebd617ac5c66b3897e9a2210d7b1c5b175657ab28f98cedf277db31088f208af8d42b8a6f4d1df57bcec3981e3ac8b6599d737d6dc7a11ee1b708dc6252b304b50cd332e4c3fdb712068fe2f3897c2115c431a6aeec55a06cc5f5ee7528c4c05639e4200da18b13ee939d91559c6afa2b696617caaf16317259a86a6d8f22ee6aa70e60f02fbe4cd4bbac026551a05d1564e0831b3d5d69e24ffce8ef89d9836cf5954bd25163d8ebfbb08193d8bff85ce330ce16fd3c5b447c0d7460c32dbd9c5a4f0a7c75baea3efd6d77dd04c143669f9358eb5ff62fd8ad0010326e5707d2ed0281d60f6be00ed99f7ebc1e2f59207a82b058ff65024d84d14018d122522be9aa55e9ba73720c158dbd4928b835361e8d5cb2c9a5cbd3c66efb2a0107030c4d9774f1fbb66ddc2232ee13695caf70dc53fa13f257bb860baf9bdb85f16514569b5049688b91d3b5e6980d1e99783c97afcbd8bc0f3a9c03a84b9352079d5ea4bff51cab7a8fbf7bddc665c53e2b6481b6680cf52a37aa7e3e015568c7b03f9ecc7200144c890a33000c074cd2f22b591712fbf2a895c491f43dd7880540f519a127855995e3b81d6a07327b630c80c764e02fb1ef7ea60b9951c8a31999b596d8ffa8249aa46ba23e3de0654b4c1aa67a40d626276f02ba44df9085042dbb5d3ae3a619c5877036dfc8d380e8c7d71ba57a5db868520212f98af64c34baef6a4a3ea6879197bca41c39078164962c8968a551487d3a1465aabdc949fbb2bd10fb8f8e008f44fd6c96550101fcae0984cfee428b10086da1c0fd920a6316aed6996cc8765e381b681892ccd958e1a5a0464320bf507c149b6e2b7d484f95b47d4c859346389b731da630bda89cb886c107eaa0295e05e0fe150fbaefc44b77333d945f6510649116db681693e4796fd99ff032b68dbef50b6ffe554dd1b2823c7b8f43ccc744096851ae7fc7abb2b871d0f26123f84e9d3d75db212d7c7d4cb50ca263d5dd276d1417f3cd81274d1a501990fd3603c1390aaeb6e8e5957cc2ca67ae7054e1d23517c409fe3702272acc9c482180cd8a73a73b86b5914d77bb48cae1cbd9e17c620f85c8d3f405768350af66e72c6f13bf3bae1a15d9ad150e303585ed8b1a3f036a1410eb30f1d63029f69ddb19536e36ce50f37288de57faa198ac72e37e67352ade8aff32ed86a93d91c21d158375dbdbe110796bb811781c12c9bc1544c1ce43d9e949278a632e7be9e0c0dace7c30f5fdcaaaf0121f741e0cbc5b6d4c785489c478b908bf1b157a9339b1a11ae05c65ffdc26a76df6c84f8b33af7c52cb02fa9ea6cbc1e7d040698f557ae8fd5b45ed8588796de05692ed576e470960d183bb02f6644d699fa68b7d2f9d1ed3df5e1202c8d61dad1fbf504bbbfbd2394f8af9418ed54fc6968ccbcb03c5d0ebeb88090b834254482a4d3b1a69e4c8e013553838a5b07ffa5f1984c965cd0f66b773edc69ec7b653b3c9fb187a0132d08e9796fe0e2834c067"
                            }
                        },
                        "amount": {
                            "value": "-8711704563008",
                            "currency": {
                                "symbol": "MCM",
                                "decimals": 9
                            }
                        }
                    },
                    {
                        "operation_identifier": {
                            "index": 1
                        },
                        "type": "TRANSFER",
                        "status": "SUCCESS",
                        "account": {
                            "address": "0x490be140603e4c1db099d8124c5ba79c4f15054a9e885c46a47099615bd86012e69a411b0b6bf3b2163651f04bef8070adcf575925d7e9c55ac98ab72511cc482f2bd619557aa1f64c6dfad47e078fa8f64f172d232cffc919343d56ae2fd9ce371c2c36f46610595c2b8a889c1dcb8a06f378d2a4f039045eac968544a4a8c97c2806fd4deebb5c09ccc781c13024bffb68ec3fff5c2c8b8d4c29848346c802834da166ad6175b86dde0ac92ff794b48f2f6a31ae11657c3a7200c3dd828a0dc6567091c8862709e6eaf430b5f6b23b3768eb9a30cce47d0e07a4e0e865418c298e89b9c01a49e6e5dbdab2ce15144cd629557a54fc86671394ec24f91801dad339c844d0763ef3db80e91f5b3e190c044167841eff09384bee7a5421132c039cd694143a7dcb470f854778ef766ba6e7d376600f3b585ed0427d7389648e97e80b1f9fd9141970c1945257eec91a7cb5eaf0203ef50f399f2e9009a67b43bfab56094fa69d837527360740c1140df3d105b59910c72d5ea4b5ddce49201c757289b3965cb86f5284ff3a0b353f636b205c8e9886ae3bb6c1b2a00df41427d8b2d6b5d6259d0746cf3895b3248a7e6a78d133e910aca0a016ccb167606e330fa58dc7b644784468c66370a60c0b7068d1c4538dd0d8b01620b5c44427f1bffdd8d075bf5642124f351a22051fd2aecdae1d06bb1b9cf92c74f581e45cdcef5734b4275a584ecf42da18e7999040736c8cf40d8746f4140e1cc60a50d90471d7c9742fe1c0c2f25522a93db9ca912b1b04aafdedb9bc93e3c459b2ce883948b941c49339ea35597638d06d3661655201ed63b2fe4502104462a93da0b593bc352be77bce0be55a9c4f97790a1afc900ff04dfc11f7c56dc63c410226522b8cd01f7b161037ec8982970f62f647c817600a35126bfda045afce3c62f0746978fc4b2c2d264115a0cd2c0a27a75c9584ab4b9c3e27ec918c49989732618b60245dfab3127174904eff7fd0fa05aea325592f771c889f2555ba4c385b61de50e8e95ee0fe000780d6d7be2ec543433ba5b73e6bb46d3db781950cf17ae16fc30defc39a15cdbc0823ba730c8643b83c40693afd428a7149cc3876150e891fc2345852c2d6336e2763066cb8450ce448c99143c5c656dfb3ba52dde35d5bd1f664ea911ce634c87a801ecb341ef47f7438a03dbe53359bdf5b0cf79f236518300abe47c77f55e45b67915afa588b1d9faa1327852eabf1eadeac0269903eb8b5dfe7b778a6da4fb36c28f2a9943922dee2a794be905c4d08660211585e1a1e0e40376705b148c258a7f6918e17b5ebb812c64745371675a5d2cb42bdb8c8992d6a2711e8fe330739e201c2457304a64eeb86c220c1a6f9f95c8029a8392701016b025df71f1ef01a7e84957311c0c4c41347f3835f3c6b2d68c954bc460584ec7988e34419ead0be3ac790a7b897cdef583c840c4358ea491e019a812c1a455b2731d2b2447fb1bc3c93d8685521c11200917b27470ff6b5b7e03b6e327ad87f885d0fe040aec8c0c0aa76a92566185c109e1569ecafa98ab284a7166e9a4dcdedc361c67a1cfa424a829767e880d20dc02f46bb7bef82ceb00a0fb4b5f58e8076ced49783dbbc2fbda3c3313d3e747b2b2bef261e5b1dab2408e292cdb39d1f9d7c8df626ade3693631fbc5ee6bcb328b796ab85e76c3265a61b8558d2ecd00bc9baf2aebe7ded5407e25440d4c19d8cc51fd898b00f4c6931d2fa70725d206a3928d0003fa6c041c61ad8c9fc3f34a337061355729ff0d2973ecf7ca9bc6aee6dd32c4f8a18e919778b5587260c055e42bc0d24630a36fabc7bd040417401a89094ab983fa2bf86c57f71df342578061132ef73757d03b74858e925da35b17fcb5dd829c180115b98834c802b06a16638e60a13a73424d2be6b86e803cf4d07a49a8bfa79465840cf6a12a02ecfb4b3f7b4a023c511f30465f80fd94c64a2b65c9de2e40223ef1dbb55770eb296d31f61b39e9229d99197fd489034c55fef20e723b9ba3c9167614fb49579794abf2296fe973a6dada56a027776b245a430f5f356a80dfef6a7ccac9ce378a4ac0e06686f6c8efe9b6691669005754542cd3f9e8d105894cf673cbdfc0e0061ed0d8dbbdb12a43be827c6f98ea5086ff2ef5f34334b6a055549df15e9d6c2ca426b09571db2ca5189ba29e67823cf9fb87c954e8924c3f32a2df788b140bbec89fec6ef86198710f3ec2ad3fd4f955f5f277a1d69f0e7127009254b49772e418089f2c8a1b91c8a1b86d65f95587e11bd6ca08582ed2ae8df2df14759d02d01bc173a1e2692abf9ba9c7c8a3b7829ff627f0c57327ee6ee49c206fde7869c66b4941137ec7cab7dd30ec2da22ad8da80c90f06d7d9b57925b2a6a3f9d641162cc3ca0de58ddd2d7786959d35cdf9503f499a3b673532f194f6abd7676bbfd2c632911b15e2deada9ce5c39ba8bb800a38963f85d4d99d7c1117593175da87d2c876f2affce17022d42a6bde40a702889e21ab1939181844f56581e86d6acce1baa22e3475db8dbc684409bc157fab189b4de942243aa3a0f85a665ece709ec4fcd3d85c26ae6f5e35afb27512ab79a5e597684c44e575efb958eeb0c3a1f8039e0dce1e8960f410220f87903bf5c7bac91721e6a509b1856b0f9cd00d2832659225f62f013b134a6bcd04662841b6802e2ac4a837789c5e7a323c998964f086930fd8c17078e785ba4de3baa36551a71b8ca51d468f3b8248d94eafbbf794fab0435b812a353bd6cc3539287c54da1bd3851d37af6583c4be0763390aed7b0d6ecac28f4881e926090576bc2d196f283a76fc5af3af3c977be25401fba976d9b1f70f3accca416398283a541ff4e8831c27183648e37db72d7a5409080fc2336c683571f8d6e77d180e264043d9fc8c50e38814b0152b4a9a806b76d78debc9cf8ba422bdd2e6b45c2e865023033e6bdf2434fe7b71f2c488e19a8a8c529bd32ed8d5430e3e5fe425cfe65b9041d70ff111311d4332f4ea9b01a4c020b27645b18cda4cb258b7587563ca5eb51376edca053373f0952faccedcef6173c21ef477b60d84b8a459b51420000000e00000001000000"
                        },
                        "amount": {
                            "value": "1000000000",
                            "currency": {
                                "symbol": "MCM",
                                "decimals": 9
                            }
                        }
                    },
                    {
                        "operation_identifier": {
                            "index": 2
                        },
                        "type": "TRANSFER",
                        "status": "SUCCESS",
                        "account": {
                            "address": "0x0132d08e9796fe0e2834c067",
                            "metadata": {
                                "full_address": "0xadb2a75424dad5c349adb4c66079f22da5c9c42cfb5c211b2382e17313c7e285e97206ef07917266e9a0f6648323924eae8ccf4f8f3d583016a41991509f5b80617cba563fb360ee6a5ae33804f156d6e08746ce455c902af98ece89456f4713d1c8002267bb9a2b37eddff298dc215c7d12f8d39ad6e142edb06002f4ee1bdd5e41f7acd8039e952bd6a1f7bcb1a07e4ccf10ef2e13bb478c3661921b6662768c274aab322d62e075d62654a2cf5c4b4f3f231c175019a8215a5374061a36abfd588231e2eac10b47b709a62b137ab08456862a5a716b6193953dc63167a6278cc2705f3af8ab65f0656ef2c8bfaf05fa96daaa9f7c05fdb0c711a9775ea3483785d2aab57fd271adb9ec8dcb5858b920f2047a12522d41f2a30d1f706f6caf8f9a837d5e2b096533d3fccf7939e89a26df7d5b73b93b144c0bcdb97a46b4fe193e4dfb85be7cc9d7d1f92206420e8c32ae64403b4321f601ad9aab347f2816dccb805617ffc2efcf65cf5de38523965d22b366549e067faa02eb335f9ab6667f8484fd565ca1c723bf756d62c2296dda89682f9c18ce9d5dc7b367e34e7643cfdfdf4023d174d3975fa7818a637e2620b0745891b105102c0135c0ed4a1a61bcbc8826b75725c3c91a365c226eb03941623e3e9daa25c2abcd4446f1b78793d11ae07f65f6c271070914ac93dd11a796d91e18b960a40586964c5026a5eb01cd73ae2b4927346e2778d6f1f0bd1d2f04a45edadd526eba26d867dd3ff43f2178ffd91ccdb84293c1432cd1de426c1982bb63d1895dc7f215db3fa6137263e7939323ae179c34e2a982012a2ee82dca62d74623882d64da22d112d93057e192a25944930d73f6911f0fcff6dbe77b6dbab6461e0611d2ca3265a8acb9d66f7a0533eee280c51dee603a9a8826857034159b16aee2e332fbea138dd26407eac81de7524a116566e276d895ae5099569b0285cb8416b4c85a5a444bae783efe0448579ee11a28bb0066762b979a358e5a67f2c040c8a08f1bab1fe60d0bf060c0fbdc8af2d97f28d58ee54807b05c0f2fcf54300f691a653afe70ae8c1f1bd3c719fefd868635dbc3a24f3c87f80d058c113479288959b5afe886c9624174f3a29fe7b6e50b790371c3e014c5b249d692628da4b18ddfe2caf707f90a3fdeda77b1f9f40a336a43e9173ccf4ae5bc9d84c5baa8001cdf59009eb103a15b98a673ad14ae0bd7a431ce9fcae786f2a9959a81c03f6b701abb8e38d40c63d4373129e46419778c9726f3df3c352efa2b56c5f4001638b1c4f60730d31185ac1c89802aff33889c0ae9b3e99aedcade4ec3d18b70164a5c91c36cedf9ae0fe7ed2716a411824eadc78be43fff146f2283303fff31c4ef4f14458d3ec79e53cbfb2dab79516dbb4c5918fadf1fe71cdbb11ae1d9fb3aeb930f624b5a12206adc0f282c689cea4e95318a372404feb6fa93b755b6d0ef359c21758ae2e4dc4706820f55869ad180a2a3a6c53c1d17518485d920b2d19bdbc1cf3c90b9636e5e7d1d03b0cfa5d7f94c1df3d3291158616e0aa48c6169275b705630bdd5942971d39e032a0d97398781f9dbcbc7078550dc016a1f5d855c329940930a5e549a65d80bb717a3402dc7688dce84d991cb677e7b7926fa7a4a0b026b210c552dcbd4ab75308021ff784b5534e78000bcf7d9372ede6b462a9141eb57aafa7679efc86c15fc722b48341aef49eabaf689de86a05f8abc68916afad85036be4c3ec5289d943d3e4ec6677399f610b1eb4843f844fc6b7b171fb874f67fab29b772af589ef8c3d22c337ed6528813fc901941eb20c4b2d6014689f3dd9ffb3747b0159a69579440bc2eb9dfd30a27494c2ee4fc8fcb3a7ca424d762889c5b48bfa5de517ff3ae3f4c8a42d60a76f961b86c4bc913ac15fef273dbea412a9c24282eb43abff7eb26b6a2c8619af348c196398982c53587da825c309fd0f91f6ac52b64bf160ce43a52927136d71864b5c38f3b4521afc8a18347e4936a10700e1e1b69c849e6ef54196384172930905c542fd36684e180c9d48b9859485902ffe3dd0e4fe6eb276da56834f7a97efefb687de5963bafa72a92e42471e7b03540be99f7151931e08740f23fecc9f6e0a15a3ae3557f733e81a3c5270049a8cd6cd8578a3b6a716139e2891f1c9ef94aabc4fc59643738ac9e9f438599ff8450ff4a19c142056f50d18f3a7012330808178f07d82aab734ecddacec720b2061567aee599a4ffc1bf038f2237479751b716b95f3b1e54123f692f71f89e58b54351384097fdeb71a96eabe6a7544120cc0bea7367c99ca3e99f015ad035ae4cb59a7391da53da01383a215037b1150a0adc0b4d58eee51452276955457d26f7114c745f68b945324825e2bb16eaef327d18f097dd84cff6eb196ebbc253292d6b784699887b4bb50e4f887181c5474ef47d4629352f85a57be73cc3053116bee8edb2bb11ecbdc1dbc876313915c1dea8afe0aba05223958efda35400e84d5e5d714362330d96d4a81e2222e679effe8c50f87432c3bbc137aff2f5830187c93e6560769af138c455c7f4773f063d5acd802f02b34a64ca3f8ae979164f7b9a23c199464e8019c6f7dd525ae977edad03891ab473130d5e4a3837e47eb7fa96b3d9f034fe85f3c943089c1163b7fbbba0862ac7a72b55fc1cd8fd9bb02dd7d85c6378acf08755c235cb8a6d602a532002cc64d2aaf466971fee5c245f360ba1128dbe506a590dd24cacbb90f3f1a60aa4c48a710fdcaa1293d98011b8891dfaf57012f5638d6efc056e61e71d77bf3d8088fe56d52c4821085c944b5607d9ec5e3b1c29ee96c49a452b211b6b65608da820e5670524d62030f972f69c56bf10f758dd7e736b066295a243a3e94eee84898a54cc90774245b79b04cdce6cf183c46cc88780e4185df6cae1335cc8064d4f3fbb133fb47a48266f8c0a79ec5aa1b65d61d2ca82b850b2198e588d09491dc4f722c4e00292c2589f6ce781b9eb178f81aa2165b1465b1e93ffb2c07fb4be3d02c742b370b5016b13dec610dacf7dd7ef1016954d8d883767973657ca742fb2f1b9821940e84d5f5adca6e8950132d08e9796fe0e2834c067"
                            }
                        },
                        "amount": {
                            "value": "8710704562508",
                            "currency": {
                                "symbol": "MCM",
                                "decimals": 9
                            }
                        }
                    }
                ],
        "metadata": {}
    }

    # Send the preprocess request
    preprocess_response = requests.post(f"{base_url}/construction/preprocess", json=preprocess_payload)
    if preprocess_response.status_code != 200:
        print("Preprocess failed:", preprocess_response.json())
        return

    # Extract options from the preprocess response
    preprocess_result = preprocess_response.json()
    options = preprocess_result.get("options", {})

    # Define the metadata request payload
    metadata_payload = {
        "network_identifier": {
            "blockchain": "mochimo",
            "network": "mainnet"
        },
        "options": options
    }

    # Print the metadata request payload
    print("Metadata Request Payload:", json.dumps(metadata_payload, indent=4))

    # Send the metadata request
    metadata_response = requests.post(f"{base_url}/construction/metadata", json=metadata_payload)
    if metadata_response.status_code != 200:
        print("Metadata request failed:", metadata_response.json())
        return

    # Print the metadata response
    metadata_result = metadata_response.json()
    print("Metadata Response:", json.dumps(metadata_result, indent=4))

# Run the test
if __name__ == "__main__":
    test_construction_preprocess_and_metadata()

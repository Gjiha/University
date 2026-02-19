/*
Copyright 2020 IBM All Rights Reserved.
SPDX-License-Identifier: Apache-2.0

Copyright 2023-2023 Franco Arcieri All Rights Reserved.
SPDX-License-Identifier: Apache-2.0
*/

package main

import "C"

import (
	b64 "encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"time"

	"github.com/hyperledger/fabric-sdk-go/pkg/core/config"
	"github.com/hyperledger/fabric-sdk-go/pkg/gateway"
	// "encoding/json"
	// "fmt"
	// "os"
	// "time"
	// "github.com/hyperledger/fabric-protos-go-apiv2/gateway"
)


type CmdAddKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
	Value     string   `json:"value"`
}
type RemoteCmdAddKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
	Value     string   `json:"value"`
}
type AnsAddKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}
type RemoteAnsAddKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}

// HistoryQueryResult structure used for returning result of history query
type StructKeyHistory struct {
	Data      string    `json:"data"`
	TxId      string    `json:"txId"`
	Timestamp time.Time `json:"timestamp"`
	IsDelete  bool      `json:"isDelete"`
}
type AnsGetKeyHistory struct {
	VData     []StructKeyHistory `json:"vdata"`
	Result    bool               `json:"result" default:"false"`
	Msg       string             `json:"msg" default:""`
	TxId      string             `json:"txid" default:""`
	ChannelId string             `json:"channelid" default:""`
}

type CmdGetKeyHistory struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}

type RemoteAnsGetKeyHistory struct {
	VData     []StructKeyHistory `json:"vdata"`
	Result    bool               `json:"result" default:"false"`
	Msg       string             `json:"msg" default:""`
	TxId      string             `json:"txid" default:""`
	ChannelId string             `json:"channelid" default:""`
}

type RemoteCmdGetKeyHistory struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}

type CmdGetKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}
type RemoteCmdGetKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}
type AnsGetKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	Value     string `json:"value"`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}
type RemoteAnsGetKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	Value     string `json:"value"`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}

type CmdDelKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}
type RemoteCmdDelKV struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}
type AnsDelKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}
type RemoteAnsDelKV struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}

type CmdGetTxData struct {
	Requester string `json:"requester"`
	TxId      string `json:"txid"`
	ChannelId string `json:"channelid"`
}
type AnsGetTxData struct {
	Result bool   `json:"result" default:"false"`
	Msg    string `json:"msg" default:""`
}

type CmdGetKeys struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
	HowMany   int32    `json:"howmany" default:"1024"`
	Bookmark  string   `json:"bookmark" default:""`
}
type RemoteCmdGetKeys struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
	HowMany   int32    `json:"howmany" default:"1024"`
	Bookmark  string   `json:"bookmark" default:""`
}
type AnsGetKeys struct {
	Result    bool       `json:"result" default:"false"`
	Msg       string     `json:"msg" default:""`
	VKeys     [][]string `json:"vkeys"`
	Bookmark  string     `json:"bookmark"`
	TxId      string     `json:"txid" default:""`
	ChannelId string     `json:"channelid" default:""`
}
type RemoteAnsGetKeys struct {
	Result    bool       `json:"result" default:"false"`
	Msg       string     `json:"msg" default:""`
	VKeys     [][]string `json:"vkeys"`
	Bookmark  string     `json:"bookmark"`
	TxId      string     `json:"txid" default:""`
	ChannelId string     `json:"channelid" default:""`
}

type CmdGetNumKeys struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}
type RemoteCmdGetNumKeys struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
}

type AnsGetNumKeys struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	NumKeys   int32  `json:"numkeys"`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}
type RemoteAnsGetNumKeys struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	NumKeys   int32  `json:"numkeys"`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}

type CmdGetClasses struct {
	Requester string `json:"requester"`
}
type RemoteCmdGetClasses struct {
	Requester string `json:"requester"`
}

type AnsGetClasses struct {
	Result    bool     `json:"result" default:"false"`
	Msg       string   `json:"msg" default:""`
	Classes   []string `json:"classes"`
	TxId      string   `json:"txid" default:""`
	ChannelId string   `json:"channelid" default:""`
}
type RemoteAnsGetClasses struct {
	Result    bool     `json:"result" default:"false"`
	Msg       string   `json:"msg" default:""`
	Classes   []string `json:"classes"`
	TxId      string   `json:"txid" default:""`
	ChannelId string   `json:"channelid" default:""`
}

type ReqConnect struct {
	Requester string `json:"requester"`
	OrgId     string `json:"orgid"`
	Channel   string `json:"channel"`
	Domain    string `json:"domain"`
}

type AnsConnect struct {
	Result bool   `json:"result" default:"false"`
	Msg    string `json:"msg" default:""`
}

type CmdCloseConnect struct {
	Requester string `json:"requester"`
}
type RemoteCmdCloseConnect struct {
	Requester string `json:"requester"`
}
type AnsCloseConnect struct {
	Result bool   `json:"result" default:"false"`
	Msg    string `json:"msg" default:""`
}

type Connection struct {
	contract *gateway.Contract
	gw       *gateway.Gateway
}

var (
	connection Connection
	connected  bool = false
)

func vbtocs(vb []byte) *C.char {
	return C.CString(string(vb))
}
func cstovb(cs *C.char) []byte {
	return []byte(C.GoString(cs))
}


//export Connect
func Connect(data *C.char) *C.char {
	cmd := new(ReqConnect)
	ans := new(AnsConnect)

	if connected {
		ans.Result = true
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(data)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	orgid := cmd.OrgId
	channel := cmd.Channel
	domain := cmd.Domain
	contract_name := "fabcar"

	fmt.Printf("%s %s %s %s\n", orgid, channel, domain, contract_name)

	err = os.Setenv("DISCOVERY_AS_LOCALHOST", "false")
	if err != nil {
		ans.Msg = fmt.Sprintf("Error setting DISCOVERY_AS_LOCALHOST environemnt variable: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	if _, err := os.Stat("wallet"); err == nil {
		os.RemoveAll("wallet")
	}

	wallet, err := gateway.NewFileSystemWallet("wallet")
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to create wallet: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err = populateWallet(orgid, domain, wallet)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to populate wallet contents: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	ccpPath := filepath.Join(
		"crypto-config",
		"peerOrganizations",
		"org"+orgid+"."+domain,
		"connection-"+"org"+orgid+".yaml",
	)

	fmt.Printf("ccpPath: %v\n", ccpPath)
	gw, err := gateway.Connect(
		gateway.WithConfig(config.FromFile(filepath.Clean(ccpPath))),
		gateway.WithIdentity(wallet, "appUser"),
	)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to connect to gateway: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	network, err := gw.GetNetwork(channel)
	if err != nil {
		gw.Close()
		ans.Msg = fmt.Sprintf("Failed to get network: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	contract := network.GetContract(contract_name)
	connection.contract = contract
	connection.gw = gw

	connected = true

	//Faccio una evaluatetransaction e poi aspetto 2 secondi per dare tempo al canale di stabilizzarsi
	{
		GetClasses()
		time.Sleep(2 * time.Second)
	}

	ans.Result = true
	b, _ := json.Marshal(ans)
	return vbtocs(b)
}

//export CloseConnection
func CloseConnection(data *C.char) *C.char { //idx int) bool {
	ans := new(AnsCloseConnect)

	if !connected {
		ans.Result = false
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	connection.gw.Close()
	connected = false
	ans.Result = true
	b, _ := json.Marshal(ans)
	return vbtocs(b)
}

//export Check
func Check(data *C.char) *C.char {
	if !connected {
		return C.CString("Not connected")
	}

	result, _ := connection.contract.EvaluateTransaction("Check", C.GoString(data))
	log.Printf("Got: %v\n", string(result))
	return C.CString(string(result))
}

//export AddKV
func AddKV(req *C.char) *C.char { //idx int, classe string, key string, value string) bool {
	cmd := new(CmdAddKV)
	ans := new(AnsAddKV)

	if !connected {
		ans.Result = false
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(req)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("AAAFailed getting command: %s . %s\n", err.Error(), C.GoString(req))
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	rcmd := new(RemoteCmdAddKV)
	rans := new(RemoteAnsAddKV)

	rcmd.Requester = cmd.Requester
	rcmd.Class = cmd.Class
	rcmd.Key = cmd.Key
	rcmd.Value = cmd.Value
	//fmt.Printf("Request AddKV: %v, %v, %v\n", rcmd.Class, rcmd.Key, rcmd.Value)

	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.SubmitTransaction("AddKV", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export GetKV
func GetKV(req *C.char) *C.char { //idx int, classe string, key string) []byte] {
	cmd := new(CmdGetKV)
	ans := new(AnsGetKV)

	if !connected {
		ans.Result = false
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(req)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	classe := cmd.Class
	key := cmd.Key

	rcmd := new(RemoteCmdGetKV)
	rans := new(RemoteAnsGetKV)
	rcmd.Requester = cmd.Requester
	rcmd.Class = classe
	rcmd.Key = key
	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.EvaluateTransaction("GetKV", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.Value = rans.Value
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export GetKeyHistory
func GetKeyHistory(req *C.char) *C.char { //idx int, classe string, key string) []byte] {
	cmd := new(CmdGetKeyHistory)
	ans := new(AnsGetKeyHistory)

	if !connected {
		ans.Result = false
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(req)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	classe := cmd.Class
	key := cmd.Key

	rcmd := new(RemoteCmdGetKeyHistory)
	rans := new(RemoteAnsGetKeyHistory)
	rcmd.Requester = cmd.Requester
	rcmd.Class = classe
	rcmd.Key = key
	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.EvaluateTransaction("GetKeyHistory", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.VData = rans.VData
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export DelKV
func DelKV(req *C.char) *C.char { //idx int, classe string, key string) []byte] {
	cmd := new(CmdDelKV)
	ans := new(AnsDelKV)

	if !connected {
		ans.Result = false
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(req)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	classe := cmd.Class
	key := cmd.Key

	rcmd := new(RemoteCmdDelKV)
	rans := new(RemoteAnsDelKV)
	rcmd.Requester = cmd.Requester
	rcmd.Class = classe
	rcmd.Key = key
	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.SubmitTransaction("DelKV", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to submit transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export GetKeys
func GetKeys(data *C.char) *C.char { //idx int, classe string) (bool, []string) {
	cmd := new(CmdGetKeys)
	ans := new(AnsGetKeys)

	if !connected {
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(data)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	rcmd := new(RemoteCmdGetKeys)
	rans := new(RemoteAnsGetKeys)
	if len(cmd.Bookmark) == 0 {
		rcmd.Bookmark = cmd.Bookmark
	} else {
		b, _ := b64.StdEncoding.DecodeString(cmd.Bookmark)
		rcmd.Bookmark = string(b)
	}

	rcmd.HowMany = cmd.HowMany
	rcmd.Key = cmd.Key
	rcmd.Requester = cmd.Requester
	rcmd.Class = cmd.Class
	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.EvaluateTransaction("GetKeys", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.VKeys = rans.VKeys
	if len(rans.Bookmark) == 0 {
		ans.Bookmark = rans.Bookmark
	} else {
		ans.Bookmark = b64.StdEncoding.EncodeToString([]byte(rans.Bookmark))
	}
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export GetNumKeys
func GetNumKeys(data *C.char) *C.char { //idx int, classe string) (bool, []string) {
	cmd := new(CmdGetNumKeys)
	ans := new(AnsGetNumKeys)

	if !connected {
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	err := json.Unmarshal([]byte(C.GoString(data)), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	rcmd := new(RemoteCmdGetNumKeys)
	rans := new(RemoteAnsGetNumKeys)
	rcmd.Class = cmd.Class
	rcmd.Key = cmd.Key
	rcmd.Requester = cmd.Requester

	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.EvaluateTransaction("GetNumKeys", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.NumKeys = rans.NumKeys
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b, _ = json.Marshal(ans)
	return vbtocs(b)
}

//export GetClasses
func GetClasses() *C.char { //idx int, classe string) (bool, []string) {
	cmd := new(CmdGetClasses)
	ans := new(AnsGetClasses)

	if !connected {
		ans.Msg = "Not connected"
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}

	rcmd := new(RemoteCmdGetClasses)
	rcmd.Requester = cmd.Requester
	rans := new(RemoteAnsGetClasses)
	b, _ := json.Marshal(rcmd)
	result, err := connection.contract.EvaluateTransaction("GetClasses", string(b))
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to evaluate transaction: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	err = json.Unmarshal(result, rans)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to unmarshal: %s\n", err.Error())
		b, _ := json.Marshal(ans)
		return vbtocs(b)
	}
	ans.Msg = rans.Msg
	ans.Result = rans.Result
	ans.Classes = rans.Classes
	ans.ChannelId = rans.ChannelId
	ans.TxId = rans.TxId
	b1, _ := json.Marshal(ans)
	return vbtocs(b1)
}

func populateWallet(orgid string, domain string, wallet *gateway.Wallet) error {
	log.Println("============ Populating wallet ============")
	credPath := filepath.Join(
		"crypto-config",
		"peerOrganizations",
		"org"+orgid+"."+domain,
		"users",
		"User1@"+"org"+orgid+"."+domain,
		"msp",
	)

	certPath := filepath.Join(credPath, "signcerts", "User1@"+"org"+orgid+"."+domain+"-cert.pem")

	fmt.Printf("credPath: %v\ncertPath:%v\n", credPath, certPath)
	// read the certificate pem
	cert, err := ioutil.ReadFile(filepath.Clean(certPath))
	if err != nil {
		return err
	}

	keyDir := filepath.Join(credPath, "keystore")
	// there's a single file in this dir containing the private key
	files, err := ioutil.ReadDir(keyDir)
	if err != nil {
		return err
	}
	if len(files) != 1 {
		return fmt.Errorf("keystore folder should have contain one file")
	}
	keyPath := filepath.Join(keyDir, files[0].Name())
	fmt.Printf("Keypath: %v\n", keyPath)
	key, err := ioutil.ReadFile(filepath.Clean(keyPath))
	if err != nil {
		return err
	}

	identity := gateway.NewX509Identity("Org"+orgid+"MSP", string(cert), string(key))
	fmt.Printf("Fatto!\n")
	return wallet.Put("appUser", identity)
}

func main() {
}

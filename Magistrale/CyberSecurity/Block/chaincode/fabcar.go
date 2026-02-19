/*
SPDX-License-Identifier: Apache-2.0
© 2020 IBM All Rights Reserved.
Modified from original code by Franco Arcieri (franco.rcr@gmail.com)
© 2021-2023 Franco Arcieri All Rights Reserved.
*/

package main

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/golang/protobuf/ptypes"
	"github.com/hyperledger/fabric-contract-api-go/contractapi"
)

// SmartContract provides functions for managing a car
type SmartContract struct {
	contractapi.Contract
}

// type CmdLog struct {
// 	Requester string `json:"requester"`
// 	Id        string `json:"id"`
// 	Opcode    string `json:"opcode"`
// 	TxId      string `json:"txid"`
// 	Timestamp string `json:"timestamp"`
// 	Data      string `json:"data"`
// }

type CmdAddKV struct {
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

type CmdGetKV struct {
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
type CmdDelKV struct {
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

type CmdGetKeys struct {
	Requester string   `json:"requester"`
	Class     string   `json:"class"`
	Key       []string `json:"key"`
	HowMany   int32    `json:"howmany"`
	Bookmark  string   `json:"bookmark"`
}

type AnsGetKeys struct {
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

type AnsGetNumKeys struct {
	Result    bool   `json:"result" default:"false"`
	Msg       string `json:"msg" default:""`
	NumKeys   int32  `json:"numkeys"`
	TxId      string `json:"txid" default:""`
	ChannelId string `json:"channelid" default:""`
}

type CmdGetClasses struct {
	Requester string `json:"requester"`
}

type AnsGetClasses struct {
	Result    bool     `json:"result" default:"false"`
	Msg       string   `json:"msg" default:""`
	Classes   []string `json:"classes"`
	TxId      string   `json:"txid" default:""`
	ChannelId string   `json:"channelid" default:""`
}

const superclasses string = "_!_!_CLASSES_X_X_"

// func getFormattedTimeFromEpochMillis(z int64, zone string, style int) string {
// 	var x string
// 	secondsSinceEpoch := z / 1000
// 	unixTime := time.Unix(secondsSinceEpoch, 0)
// 	timeZoneLocation, err := time.LoadLocation(zone)
// 	if err != nil {
// 		fmt.Println("Error loading timezone:", err)
// 	}

// 	timeInZone := unixTime.In(timeZoneLocation)

// 	switch style {
// 	case 1:
// 		timeInZoneStyleOne := timeInZone.Format("Mon Jan 2 15:04:05")
// 		//Mon Aug 14 13:36:02
// 		return timeInZoneStyleOne
// 	case 2:
// 		timeInZoneStyleTwo := timeInZone.Format("02-01-2006 15:04:05")
// 		//14-08-2017 13:36:02
// 		return timeInZoneStyleTwo
// 	case 3:
// 		timeInZoneStyleThree := timeInZone.Format("2006-02-01 15:04:05")
// 		//2017-14-08 13:36:02
// 		return timeInZoneStyleThree
// 	}
// 	return x
// }

// func LogData(ctx contractapi.TransactionContextInterface, requester string, opcode string, data string) error {
// 	txId := ctx.GetStub().GetTxID()
// 	timestamp, _ := ctx.GetStub().GetTxTimestamp()

// 	aggrKeyReqTx, err := ctx.GetStub().CreateCompositeKey("LOG::"+requester, []string{txId})
// 	if err != nil {
// 		return fmt.Errorf("failed to make a composite key. %s", err.Error())
// 	}
// 	aggrKeyTxReq, err := ctx.GetStub().CreateCompositeKey("LOG::"+txId, []string{requester})
// 	if err != nil {
// 		return fmt.Errorf("failed to make a composite key. %s", err.Error())
// 	}

// 	cmd := new(CmdLog)

// 	cmd.Data = data
// 	cmd.Requester = requester
// 	cmd.Opcode = opcode
// 	t := time.Unix(timestamp.GetSeconds(), 0)
// 	strDate := t.Format(time.UnixDate)

// 	cmd.Timestamp = strDate
// 	cmd.TxId = txId
// 	cert, _ := ctx.GetClientIdentity().GetX509Certificate()
// 	cmd.Id = cert.Subject.CommonName

// 	rec, err := json.Marshal(cmd)
// 	if err != nil {
// 		return fmt.Errorf("failed composing log data. %s", err.Error())
// 	}

// 	err = ctx.GetStub().PutState(aggrKeyReqTx, rec)
// 	if err != nil {
// 		return fmt.Errorf("failed adding RequTxId log data. %s", err.Error())
// 	}
// 	ctx.GetStub().PutState(aggrKeyTxReq, rec)
// 	if err != nil {
// 		return fmt.Errorf("failed adding TxIdRequ log data. %s", err.Error())
// 	}

// 	return nil
// }

func AddClass(ctx contractapi.TransactionContextInterface, class string) error {
	//la classe già esiste?

	aggrKey, err := ctx.GetStub().CreateCompositeKey(superclasses, []string{class})
	if err != nil {
		return fmt.Errorf("failed to make a composite key. %s", err.Error())
	}
	valueAsBytes, err := ctx.GetStub().GetState(aggrKey)

	if err != nil {
		return fmt.Errorf("failed finding the composite key. %s", err.Error())
	}

	if valueAsBytes == nil {
		//la classe non esiste, la aggiungo
		uno := []byte{1} //per associare un valore alla coppia: superclasse, classe
		err = ctx.GetStub().PutState(aggrKey, uno)
		if err != nil {
			return fmt.Errorf("failed adding the composite key. %s", err.Error())
		}
	}
	return nil
}


//Check!!!
func (s *SmartContract) Check(ctx contractapi.TransactionContextInterface, value string) string {
	value += ": ok, here I'm"
	//fmt.Println("Sono in check!!!!!")
	return value
}

// Add keyvalue
func (s *SmartContract) AddKV(ctx contractapi.TransactionContextInterface, data string) *AnsAddKV {
	cmd := new(CmdAddKV)
	ans := new(AnsAddKV)
	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = "Failed getting command: %s:%s" + err.Error() + data
		return ans
	}
	fmt.Printf("A simple cycle for addkv...\n")

	//per prima cosa aggiungo la classe alla lista delle classi
	err = AddClass(ctx, cmd.Class)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to store class name in the BC: %s", err.Error())
		return ans
	}

	valueAsBytes := []byte(cmd.Value)
	aggrKey, err := ctx.GetStub().CreateCompositeKey(cmd.Class, cmd.Key)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to build the composite key: %s", err.Error())
		return ans
	}

	err = ctx.GetStub().PutState(aggrKey, valueAsBytes)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to store in the BC: %s", err.Error())
		return ans
	}

	// //log dell'operazione
	// err = LogData(ctx, cmd.Requester, "AddKV", data)
	// if err != nil {
	// 	ans.Msg = fmt.Sprintf("Failed to log request in the BC: %s", err.Error())
	// 	return ans
	// }

	ans.Result = true
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	return ans
}

// Get KeyValue
func (s *SmartContract) GetKV(ctx contractapi.TransactionContextInterface, data string) *AnsGetKV {
	cmd := new(CmdGetKV)
	ans := new(AnsGetKV)

	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s", err.Error())
		return ans
	}

	aggrKey, err := ctx.GetStub().CreateCompositeKey(cmd.Class, cmd.Key)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to build the composite key: %s", err.Error())
		return ans
	}

	valueAsBytes, err := ctx.GetStub().GetState(aggrKey)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to read from world state: %s", err.Error())
		return ans
	}

	if valueAsBytes == nil {
		ans.Msg = "Key does not exists"
		return ans
	}

	// //log dell'operazione
	// err = LogData(ctx, cmd.Requester, "GetKV", data)
	// if err != nil {
	// 	ans.Msg = fmt.Sprintf("Failed to log request in the BC: %s", err.Error())
	// 	return ans
	// }

	ans.Result = true
	ans.Value = string(valueAsBytes)
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	return ans
}

// Get KeyHistory
func (s *SmartContract) GetKeyHistory(ctx contractapi.TransactionContextInterface, data string) *AnsGetKeyHistory {
	cmd := new(CmdGetKeyHistory)
	ans := new(AnsGetKeyHistory)

	//fmt.Println("Entered in KeyHistory")

	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s", err.Error())
		return ans
	}
	//fmt.Println("Entered in KeyHistory with cmd: %v", cmd)

	aggrKey, err := ctx.GetStub().CreateCompositeKey(cmd.Class, cmd.Key)

	if err != nil {
		//fmt.Println("Failed to build the composite key: %s", err.Error())
		ans.Msg = fmt.Sprintf("Failed to build the composite key: %s", err.Error())
		return ans
	}

	resultsIterator, err := ctx.GetStub().GetHistoryForKey(aggrKey)
	if err != nil {
		//fmt.Println("Failed to find the history of the given key: %s", err.Error())
		ans.Msg = fmt.Sprintf("Failed to find the history of the given key: %s", err.Error())
		return ans
	}

	defer resultsIterator.Close()

	var records []StructKeyHistory
	for resultsIterator.HasNext() {
		fmt.Printf("A simple cycle for key history...\n")
		response, err := resultsIterator.Next()
		if err != nil {
			//fmt.Println("Failed to browse the history of the given key: %s", err.Error())
			ans.Msg = fmt.Sprintf("Failed to browse the history of the given key: %s", err.Error())
			return ans
		}

		var asset string
		if len(response.Value) > 0 {
			asset = string(response.Value)
		} else {
			asset = ""
		}

		timestamp, err := ptypes.Timestamp(response.Timestamp)
		if err != nil {
			ans.Msg = fmt.Sprintf("Unable to get the timestamp from ptypes: %s", err.Error())
			return ans
		}

		record := StructKeyHistory{
			TxId:      response.TxId,
			Timestamp: timestamp,
			Data:      asset,
			IsDelete:  response.IsDelete,
		}
		records = append(records, record)
	}

	ans.VData = records
	ans.Result = true
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	//fmt.Println("Esce da history: %v", ans)
	return ans
}

// Del KeyValue
func (s *SmartContract) DelKV(ctx contractapi.TransactionContextInterface, data string) *AnsDelKV {
	cmd := new(CmdDelKV)
	ans := new(AnsDelKV)

	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s", err.Error())
		return ans
	}

	// //Se la classe inizia con LOG::, allora non cancello!!!
	// if strings.HasPrefix(cmd.Class, "LOG::") {
	// 	ans.Msg = "You do not have privileges to delete certified log data"
	// 	return ans
	// }

	aggrKey, err := ctx.GetStub().CreateCompositeKey(cmd.Class, cmd.Key)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to build the composite key: %s", err.Error())
		return ans
	}

	err = ctx.GetStub().DelState(aggrKey)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to delete from world state: %s", err.Error())
		return ans
	}

	// //log dell'operazione
	// err = LogData(ctx, cmd.Requester, "DelKV", data)
	// if err != nil {
	// 	ans.Msg = fmt.Sprintf("Failed to log request in the BC: %s", err.Error())
	// 	return ans
	// }

	ans.Result = true
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	return ans
}

//GetKeys
func (s *SmartContract) GetKeys(ctx contractapi.TransactionContextInterface, data string) *AnsGetKeys {
	cmd := new(CmdGetKeys)
	ans := new(AnsGetKeys)

	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s", err.Error())
		return ans
	}

	iterator, metadata, err := ctx.GetStub().GetStateByPartialCompositeKeyWithPagination(cmd.Class, cmd.Key, cmd.HowMany, cmd.Bookmark)

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to get keys: %s", err.Error())
		return ans
	}

	var vkeys = [][]string{}

	for iterator.HasNext() {
		ckey, err := iterator.Next()
		if err != nil {
			break
		}
		_, key, err := ctx.GetStub().SplitCompositeKey(ckey.GetKey())
		if err != nil {
			break
		}
		vkeys = append(vkeys, key)
	}

	iterator.Close()
	ans.Result = true
	ans.VKeys = vkeys
	ans.Bookmark = metadata.Bookmark
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	return ans
}

//GetNumKeys
func (s *SmartContract) GetNumKeys(ctx contractapi.TransactionContextInterface, data string) *AnsGetNumKeys {
	cmd := new(CmdGetNumKeys)
	ans := new(AnsGetNumKeys)

	err := json.Unmarshal([]byte(data), cmd)
	if err != nil {
		ans.Msg = fmt.Sprintf("Failed getting command: %s", err.Error())
		return ans
	}

	var howMany int32 = 1000
	var bookmark string = ""
	var count int32 = 0
	for {
		iterator, metadata, err := ctx.GetStub().GetStateByPartialCompositeKeyWithPagination(cmd.Class, cmd.Key, howMany, bookmark)
		if err != nil {
			ans.Msg = fmt.Sprintf("Failed to get keys: %s", err.Error())
			iterator.Close()
			return ans
		}

		if metadata.FetchedRecordsCount <= 0 {
			iterator.Close()
			ans.Result = true
			ans.NumKeys = count
			ans.ChannelId = ctx.GetStub().GetChannelID()
			ans.TxId = ctx.GetStub().GetTxID()
			return ans
		}

		for iterator.HasNext() {
			_, err := iterator.Next()
			if err != nil {
				break
			}
			count = count + 1
		}
		bookmark = metadata.Bookmark
		iterator.Close()

		if metadata.FetchedRecordsCount < howMany {
			ans.Result = true
			ans.NumKeys = count
			ans.ChannelId = ctx.GetStub().GetChannelID()
			ans.TxId = ctx.GetStub().GetTxID()
			return ans
		}
	}
}

//GetClasses
func (s *SmartContract) GetClasses(ctx contractapi.TransactionContextInterface) *AnsGetClasses {
	ans := new(AnsGetClasses)

	iterator, err := ctx.GetStub().GetStateByPartialCompositeKey(superclasses, []string{})

	if err != nil {
		ans.Msg = fmt.Sprintf("Failed to get classes: %s", err.Error())
		return ans
	}

	var vkeys []string

	for iterator.HasNext() {
		ckey, err := iterator.Next()
		if err != nil {
			break
		}
		_, key, err := ctx.GetStub().SplitCompositeKey(ckey.GetKey())
		if err != nil {
			break
		}
		vkeys = append(vkeys, key[0])
	}

	iterator.Close()
	ans.Result = true
	ans.Classes = vkeys
	ans.ChannelId = ctx.GetStub().GetChannelID()
	ans.TxId = ctx.GetStub().GetTxID()
	return ans
}

func (s *SmartContract) InitLedger(ctx contractapi.TransactionContextInterface) error {
	return nil
}

func main() {

	chaincode, err := contractapi.NewChaincode(new(SmartContract))

	if err != nil {
		fmt.Printf("Error create fabcar chaincode: %s", err.Error())
		return
	}

	if err := chaincode.Start(); err != nil {
		fmt.Printf("Error starting fabcar chaincode: %s", err.Error())
	}
}

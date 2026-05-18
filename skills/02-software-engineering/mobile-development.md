---
tags: [skills, skills-eng, mobile, react-native, flutter, ios, android, mobile-architecture]
updated: 2026-05-16
title: "Desenvolvimento Mobile - React Native, Flutter e Padroes Nativos"
date: 2026-05-16
---

# Desenvolvimento Mobile

Referencia completa para desenvolvimento mobile cross-platform (React Native e Flutter), desenvolvimento nativo (iOS/Android), arquitetura mobile, testes, deploy e otimizacao de performance. Guia pratico para treinamento do agente JARVIS.

## Frameworks Cross-Platform

### Comparacao

| Caracteristica | React Native | Flutter |
|----------------|-------------|---------|
| Linguagem | TypeScript/JavaScript | Dart |
| Renderizacao | Componentes nativos | Canvas proprio (Skia/Impeller) |
| Arquitetura | Bridge ou New Architecture (Fabric/TurboModules) | Widget -> Element -> RenderObject |
| Hot Reload | Sim | Sim (Stateful Hot Reload) |
| Performance | Boa (bridge pode ser gargalo) | Excelente (compilacao AOT) |
| Ecossistema | NPM (enorme) | pub.dev (crescendo) |
| Curva de aprendizado | Baixa (se sabe React) | Media (Dart + widgets) |
| Tamanho do app | Medio (~15-30MB) | Maior (~20-40MB) |
| Comunidade | Muito grande | Grande e ativa |
| Empresas usando | Meta, Shopify, Discord | Google, BMW, Toyota |

### Arquitetura React Native

```
Old Architecture (Bridge):
┌─────────────────┐     JSON Messages     ┌─────────────────┐
│   JavaScript    │ <==================> │     Native      │
│   Thread        │     (async queue)     │     Thread      │
│                 │                       │                 │
│  React Components                      │  UIView/Android  │
│  State Management                      │  Views           │
└─────────────────┘                       └─────────────────┘

New Architecture (Fabric + TurboModules + JSI):
┌─────────────────┐     JSI (sync)        ┌─────────────────┐
│   JavaScript    │ <==================> │     Native      │
│   Thread        │   C++ bindings        │     Thread      │
│                 │                       │                 │
│  React Components                      │  UIView/Android  │
│  Concurrent Renderer                   │  Views           │
└─────────────────┘                       └─────────────────┘
```

### Arquitetura Flutter

```
┌──────────────────────────────────────────────┐
│                 App (Dart)                    │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │ Widgets  │->│ Elements │->│ RenderObj  │  │
│  │ (config) │  │ (tree)   │  │ (layout)   │  │
│  └──────────┘  └──────────┘  └────────────┘  │
└──────────────────────┬───────────────────────┘
                       │
┌──────────────────────▼───────────────────────┐
│                 Engine (C++)                  │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │  Skia/   │  │   Text   │  │   Dart     │  │
│  │ Impeller │  │ Layout   │  │   Runtime  │  │
│  └──────────┘  └──────────┘  └────────────┘  │
└──────────────────────┬───────────────────────┘
                       │
┌──────────────────────▼───────────────────────┐
│              Platform (iOS/Android)           │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │  Core    │  │  ANative │  │   OpenGL/  │  │
│  │  Graphics│  │  Window  │  │   Metal    │  │
│  └──────────┘  └──────────┘  └────────────┘  │
└──────────────────────────────────────────────┘
```

## React Native Deep Dive

### Componentes e Hooks

```typescript
import { useState, useEffect, useCallback, useMemo } from "react";
import {
  View, Text, FlatList, StyleSheet,
  TouchableOpacity, ActivityIndicator, RefreshControl
} from "react-native";

interface Usuario {
  id: string;
  nome: string;
  email: string;
  avatar: string;
}

function ListaUsuarios() {
  const [usuarios, setUsuarios] = useState<Usuario[]>([]);
  const [carregando, setCarregando] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const carregarUsuarios = useCallback(async () => {
    setCarregando(true);
    try {
      const res = await fetch("https://api.exemplo.com/usuarios");
      const dados = await res.json();
      setUsuarios(dados);
    } catch (error) {
      console.error("Erro ao carregar usuarios:", error);
    } finally {
      setCarregando(false);
      setRefreshing(false);
    }
  }, []);

  useEffect(() => {
    carregarUsuarios();
  }, [carregarUsuarios]);

  const onRefresh = useCallback(() => {
    setRefreshing(true);
    carregarUsuarios();
  }, [carregarUsuarios]);

  const renderItem = useMemo(() => (
    ({ item }: { item: Usuario }) => (
      <TouchableOpacity style={styles.item}>
        <Text style={styles.nome}>{item.nome}</Text>
        <Text style={styles.email}>{item.email}</Text>
      </TouchableOpacity>
    )
  ), []);

  if (carregando) {
    return <ActivityIndicator size="large" style={styles.center} />;
  }

  return (
    <FlatList
      data={usuarios}
      keyExtractor={item => item.id}
      renderItem={renderItem}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
      }
      contentContainerStyle={styles.lista}
    />
  );
}

const styles = StyleSheet.create({
  center: { flex: 1, justifyContent: "center" },
  lista: { padding: 16 },
  item: {
    padding: 16,
    backgroundColor: "#fff",
    borderRadius: 8,
    marginBottom: 8,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  nome: { fontSize: 16, fontWeight: "bold" },
  email: { fontSize: 14, color: "#666", marginTop: 4 },
});
```

### Navegacao com React Navigation v6

```typescript
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { Ionicons } from "@expo/vector-icons";

// Tipos das rotas
type RootStackParamList = {
  Auth: undefined;
  Main: undefined;
  Detalhes: { id: string };
};

type MainTabParamList = {
  Home: undefined;
  Busca: undefined;
  Perfil: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();
const Tab = createBottomTabNavigator<MainTabParamList>();

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          const icons: Record<string, string> = {
            Home: focused ? "home" : "home-outline",
            Busca: focused ? "search" : "search-outline",
            Perfil: focused ? "person" : "person-outline",
          };
          return <Ionicons name={icons[route.name]} size={size} color={color} />;
        },
        headerShown: false,
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Busca" component={BuscaScreen} />
      <Tab.Screen name="Perfil" component={PerfilScreen} />
    </Tab.Navigator>
  );
}

function Navegacao() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Auth" component={AuthStack} />
        <Stack.Screen name="Main" component={MainTabs} />
        <Stack.Screen name="Detalhes" component={DetalhesScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

// Navegacao programatica
function HomeScreen({ navigation }: any) {
  return (
    <TouchableOpacity onPress={() => navigation.navigate("Detalhes", { id: "123" })}>
      <Text>Ver Detalhes</Text>
    </TouchableOpacity>
  );
}
```

### Gerenciamento de Estado com Zustand

```typescript
import { create } from "zustand";
import { persist, createJSONStorage } from "zustand/middleware";
import AsyncStorage from "@react-native-async-storage/async-storage";

interface AuthState {
  token: string | null;
  usuario: { id: string; nome: string; email: string } | null;
  autenticado: boolean;
  login: (email: string, senha: string) => Promise<void>;
  logout: () => void;
  atualizarPerfil: (dados: Partial<{ nome: string; email: string }>) => void;
}

const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      usuario: null,
      autenticado: false,

      login: async (email: string, senha: string) => {
        const res = await fetch("https://api.exemplo.com/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, senha }),
        });
        const dados = await res.json();
        set({
          token: dados.token,
          usuario: dados.usuario,
          autenticado: true,
        });
      },

      logout: () => set({ token: null, usuario: null, autenticado: false }),

      atualizarPerfil: (dados) =>
        set((state) => ({
          usuario: state.usuario ? { ...state.usuario, ...dados } : null,
        })),
    }),
    {
      name: "auth-storage",
      storage: createJSONStorage(() => AsyncStorage),
    }
  )
);

// Uso em componente
function PerfilScreen() {
  const { usuario, logout, atualizarPerfil } = useAuthStore();

  return (
    <View>
      <Text>{usuario?.nome}</Text>
      <Text>{usuario?.email}</Text>
      <TouchableOpacity onPress={logout}>
        <Text>Sair</Text>
      </TouchableOpacity>
    </View>
  );
}
```

### Modulos Nativos e Bridging

```typescript
// React Native - Native Module (TypeScript side)
import { NativeModules } from "react-native";

interface BiometriaModule {
  verificarBiometria(): Promise<boolean>;
  getHardwareInfo(): Promise<{ modelo: string; versao: string }>;
}

const { BiometriaModule } = NativeModules;

async function autenticar(): Promise<boolean> {
  return await BiometriaModule.verificarBiometria();
}

// iOS Native Module (Swift)
/*
@objc(BiometriaModule)
class BiometriaModule: NSObject {
  @objc
  func verificarBiometria(_ resolve: @escaping RCTPromiseResolveBlock,
                          rejecter reject: @escaping RCTPromiseRejectBlock) {
    let context = LAContext()
    var error: NSError?
    if context.canEvaluatePolicy(.deviceOwnerAuthenticationWithBiometrics, error: &error) {
      context.evaluatePolicy(.deviceOwnerAuthenticationWithBiometrics,
                             localizedReason: "Autenticar") { success, _ in
        resolve(success)
      }
    } else {
      reject("NO_BIOMETRY", "Biometria nao disponivel", error)
    }
  }
}
*/

// Android Native Module (Kotlin)
/*
class BiometriaModule(reactContext: ReactApplicationContext) :
  ReactContextBaseJavaModule(reactContext) {

  override fun getName() = "BiometriaModule"

  @ReactMethod
  fun verificarBiometria(promise: Promise) {
    val context = reactApplicationContext
    val biometricManager = BiometricManager.from(context)
    when (biometricManager.canAuthenticate(BiometricManager.Authenticators.BIOMETRIC_STRONG)) {
      BiometricManager.BIOMETRIC_SUCCESS -> promise.resolve(true)
      else -> promise.resolve(false)
    }
  }
}
*/
```

## Flutter Deep Dive

### Widget Tree e State Management

```dart
// Widget Tree: declaracao
// Element Tree: instancia
// RenderObject Tree: layout e pintura

// Provider - State Management
import 'package:provider/provider.dart';

class UsuarioProvider with ChangeNotifier {
  String? _nome;
  String? get nome => _nome;

  void atualizarNome(String novoNome) {
    _nome = novoNome;
    notifyListeners(); // Notifica widgets ouvintes
  }
}

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (_) => UsuarioProvider(),
      child: const MyApp(),
    ),
  );
}

class TelaPerfil extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final provider = context.watch<UsuarioProvider>();
    return Text(provider.nome ?? 'Sem nome');
  }
}
```

### Exemplo CRUD com Local Storage

```dart
import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class Tarefa {
  final int? id;
  final String titulo;
  final bool concluida;

  Tarefa({this.id, required this.titulo, this.concluida = false});

  Map<String, dynamic> toMap() {
    return {'id': id, 'titulo': titulo, 'concluida': concluida ? 1 : 0};
  }

  factory Tarefa.fromMap(Map<String, dynamic> map) {
    return Tarefa(
      id: map['id'],
      titulo: map['titulo'],
      concluida: map['concluida'] == 1,
    );
  }
}

class TarefaDatabase {
  static Database? _db;

  static Future<Database> get database async {
    if (_db != null) return _db!;
    _db = await openDatabase(
      join(await getDatabasesPath(), 'tarefas.db'),
      onCreate: (db, version) {
        db.execute(
          'CREATE TABLE tarefas(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, concluida INTEGER)',
        );
      },
      version: 1,
    );
    return _db!;
  }

  static Future<List<Tarefa>> listar() async {
    final db = await database;
    final maps = await db.query('tarefas');
    return maps.map((m) => Tarefa.fromMap(m)).toList();
  }

  static Future<int> inserir(Tarefa tarefa) async {
    final db = await database;
    return db.insert('tarefas', tarefa.toMap());
  }

  static Future<int> atualizar(Tarefa tarefa) async {
    final db = await database;
    return db.update(
      'tarefas',
      tarefa.toMap(),
      where: 'id = ?',
      whereArgs: [tarefa.id],
    );
  }

  static Future<int> remover(int id) async {
    final db = await database;
    return db.delete('tarefas', where: 'id = ?', whereArgs: [id]);
  }
}

class TelaTarefas extends StatefulWidget {
  @override
  _TelaTarefasState createState() => _TelaTarefasState();
}

class _TelaTarefasState extends State<TelaTarefas> {
  List<Tarefa> _tarefas = [];

  @override
  void initState() {
    super.initState();
    _carregarTarefas();
  }

  Future<void> _carregarTarefas() async {
    final tarefas = await TarefaDatabase.listar();
    setState(() => _tarefas = tarefas);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Tarefas')),
      body: ListView.builder(
        itemCount: _tarefas.length,
        itemBuilder: (context, index) {
          final tarefa = _tarefas[index];
          return ListTile(
            title: Text(tarefa.titulo),
            trailing: Checkbox(
              value: tarefa.concluida,
              onChanged: (valor) async {
                await TarefaDatabase.atualizar(
                  Tarefa(id: tarefa.id, titulo: tarefa.titulo, concluida: valor!),
                );
                _carregarTarefas();
              },
            ),
            onLongPress: () async {
              await TarefaDatabase.remover(tarefa.id!);
              _carregarTarefas();
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () async {
          await TarefaDatabase.inserir(Tarefa(titulo: 'Nova tarefa'));
          _carregarTarefas();
        },
        child: Icon(Icons.add),
      ),
    );
  }
}
```

### Platform Channels para Codigo Nativo

```dart
// Flutter side
import 'package:flutter/services.dart';

class BateriaService {
  static const platform = MethodChannel('com.app/bateria');

  static Future<int> get nivelBateria async {
    try {
      final result = await platform.invokeMethod<int>('getNivelBateria');
      return result ?? 0;
    } on PlatformException catch (e) {
      throw Exception('Erro ao obter nivel: ${e.message}');
    }
  }
}

// Android side (Kotlin)
/*
class MainActivity: FlutterActivity() {
  private val CHANNEL = "com.app/bateria"

  override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
    super.configureFlutterEngine(flutterEngine)
    MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler {
      call, result ->
      if (call.method == "getNivelBateria") {
        val bm = getSystemService(Context.BATTERY_SERVICE) as BatteryManager
        result.success(bm.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY))
      } else {
        result.notImplemented()
      }
    }
  }
}
*/

// iOS side (Swift)
/*
@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {
  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let controller = window?.rootViewController as! FlutterViewController
    let channel = FlutterMethodChannel(name: "com.app/bateria",
                                       binaryMessenger: controller.binaryMessenger)
    channel.setMethodCallHandler { call, result in
      if call.method == "getNivelBateria" {
        UIDevice.current.isBatteryMonitoringEnabled = true
        result(Int(UIDevice.current.batteryLevel * 100))
      } else {
        result(FlutterMethodNotImplemented)
      }
    }
    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
*/
```

## Desenvolvimento Nativo

### iOS - Swift e SwiftUI

```swift
// SwiftUI - View basica
struct TelaUsuario: View {
  @State private var nome = ""
  @State private var email = ""

  var body: some View {
    Form {
      Section(header: Text("Informacoes")) {
        TextField("Nome", text: $nome)
        TextField("Email", text: $email)
          .keyboardType(.emailAddress)
      }
      Section {
        Button("Salvar") {
          salvarUsuario()
        }
      }
    }
    .navigationTitle("Usuario")
  }

  private func salvarUsuario() {
    // Persistir dados
  }
}

// UIKit - ViewController classico
class UsuarioViewController: UIViewController {
  private let tableView = UITableView()
  private var usuarios: [Usuario] = []

  override func viewDidLoad() {
    super.viewDidLoad()
    title = "Usuarios"
    view.addSubview(tableView)
    tableView.delegate = self
    tableView.dataSource = self
    carregarUsuarios()
  }
}
```

### Android - Kotlin e Jetpack Compose

```kotlin
// Jetpack Compose - View basica
@Composable
fun TelaUsuario(
  viewModel: UsuarioViewModel = viewModel()
) {
  var nome by remember { mutableStateOf("") }
  var email by remember { mutableStateOf("") }

  Column(modifier = Modifier.padding(16.dp)) {
    OutlinedTextField(
      value = nome,
      onValueChange = { nome = it },
      label = { Text("Nome") },
      modifier = Modifier.fillMaxWidth()
    )
    Spacer(modifier = Modifier.height(8.dp))
    OutlinedTextField(
      value = email,
      onValueChange = { email = it },
      label = { Text("Email") },
      modifier = Modifier.fillMaxWidth()
    )
    Spacer(modifier = Modifier.height(16.dp))
    Button(
      onClick = { viewModel.salvar(nome, email) },
      modifier = Modifier.fillMaxWidth()
    ) {
      Text("Salvar")
    }
  }
}

// ViewModel
class UsuarioViewModel : ViewModel() {
  private val _usuarios = MutableStateFlow<List<Usuario>>(emptyList())
  val usuarios: StateFlow<List<Usuario>> = _usuarios

  fun salvar(nome: String, email: String) {
    viewModelScope.launch {
      // Salvar no repositorio
    }
  }
}
```

### Quando Usar Nativo vs Cross-Platform

| Criterio | Nativo | Cross-Platform |
|----------|--------|----------------|
| Performance maxima | Sim | Parcial (Flutter proximo) |
| Acesso a APIs novas do SO | Imediato | Depende do framework |
| App com muita animacao customizada | Melhor | Flutter bom, RN limitado |
| Time com experiencia web | Nao | React Native ideal |
| Budget limitado | Nao (2 times) | Sim (1 time) |
| App simples/medio | Overkill | Ideal |
| Integracao com hardware especifico | Melhor | Requer modulo nativo |

## Arquitetura Mobile

### MVVM para Mobile

```
View (UI) <---> ViewModel <---> Model (Repository)
    |                |                 |
    v                v                 v
  Observa         Transforma        Busca dados
  estado          dados para UI     (API, DB)
```

```typescript
// React Native - Arquitetura MVVM com Zustand
// Model (Repository)
class UsuarioRepository {
  async buscar(id: string): Promise<Usuario> {
    const res = await fetch(`/api/usuarios/${id}`);
    return res.json();
  }

  async salvar(usuario: Usuario): Promise<void> {
    await fetch(`/api/usuarios/${usuario.id}`, {
      method: "PUT",
      body: JSON.stringify(usuario),
    });
  }
}

// ViewModel (Store)
interface UsuarioViewModel {
  usuario: Usuario | null;
  carregando: boolean;
  erro: string | null;
  carregar: (id: string) => Promise<void>;
  salvar: (usuario: Usuario) => Promise<void>;
}

const useUsuarioVM = create<UsuarioViewModel>((set) => ({
  usuario: null,
  carregando: false,
  erro: null,
  carregar: async (id) => {
    set({ carregando: true, erro: null });
    try {
      const usuario = await new UsuarioRepository().buscar(id);
      set({ usuario, carregando: false });
    } catch (e) {
      set({ erro: "Erro ao carregar", carregando: false });
    }
  },
  salvar: async (usuario) => {
    set({ carregando: true, erro: null });
    try {
      await new UsuarioRepository().salvar(usuario);
      set({ usuario, carregando: false });
    } catch (e) {
      set({ erro: "Erro ao salvar", carregando: false });
    }
  },
}));
```

### Clean Architecture em Mobile

```
┌──────────────────────────────────────────┐
│           Presentation Layer             │
│  ┌────────┐  ┌──────────┐  ┌─────────┐  │
│  │ Screens│  │ViewModels│  │  State  │  │
│  └────────┘  └──────────┘  └─────────┘  │
└──────────────────┬───────────────────────┘
                   │ (Use Cases)
┌──────────────────▼───────────────────────┐
│            Domain Layer                   │
│  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │ Use Cases│  │Entities  │  │Repos.  │  │
│  │          │  │          │  │Interfaces│ │
│  └──────────┘  └──────────┘  └────────┘  │
└──────────────────┬───────────────────────┘
                   │ (Implementations)
┌──────────────────▼───────────────────────┐
│             Data Layer                    │
│  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │  API     │  │ Database │  │  Cache │  │
│  │Repository│  │Repository│  │Repository│ │
│  └──────────┘  └──────────┘  └────────┘  │
└──────────────────────────────────────────┘
```

## Padroes Especificos para Mobile

### Offline-First com Banco Local

```typescript
// React Native - Offline-first com SQLite
import SQLite from "react-native-sqlite-storage";
import NetInfo from "@react-native-community/netinfo";

class OfflineFirstRepository {
  private db: SQLite.SQLiteDatabase;

  constructor() {
    this.db = SQLite.openDatabase({ name: "app.db" });
  }

  async getItens(): Promise<Item[]> {
    const online = await this.verificarConexao();

    if (online) {
      // Buscar da API e sincronizar com local
      const itens = await this.buscarDaAPI();
      await this.salvarLocal(itens);
      return itens;
    }

    // Buscar do banco local
    return this.buscarLocal();
  }

  async criarItem(item: Omit<Item, "id">): Promise<void> {
    const online = await this.verificarConexao();

    // Sempre salvar local primeiro
    const id = await this.salvarLocalItem(item);

    if (online) {
      // Sincronizar com API
      await this.enviarParaAPI({ ...item, id });
    } else {
      // Marcar para sincronizacao posterior
      await this.marcarPendente(id, "criar");
    }
  }

  private async verificarConexao(): Promise<boolean> {
    const state = await NetInfo.fetch();
    return state.isConnected ?? false;
  }

  private async sincronizarPendentes(): Promise<void> {
    const pendentes = await this.buscarPendentes();
    for (const p of pendentes) {
      try {
        await this.enviarParaAPI(p.dados, p.operacao);
        await this.removerPendente(p.id);
      } catch {
        // Manter na fila para proxima tentativa
      }
    }
  }
}
```

### Push Notifications (FCM e APNs)

```typescript
// React Native - Push Notifications com Firebase
import messaging from "@react-native-firebase/messaging";
import notifee, { AndroidImportance } from "@notifee/react-native";

async function configurarNotificacoes() {
  // Solicitar permissao
  const authStatus = await messaging().requestPermission();
  const habilitado =
    authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
    authStatus === messaging.AuthorizationStatus.PROVISIONAL;

  if (!habilitado) return;

  // Obter token FCM
  const token = await messaging().getToken();
  console.log("FCM Token:", token);

  // Enviar token para o servidor
  await fetch("/api/push/token", {
    method: "POST",
    body: JSON.stringify({ token }),
  });

  // Listener para notificacoes em foreground
  messaging().onMessage(async (remoteMessage) => {
    await notifee.displayNotification({
      title: remoteMessage.notification?.title,
      body: remoteMessage.notification?.body,
      android: {
        channelId: "default",
        importance: AndroidImportance.HIGH,
      },
    });
  });

  // Listener para toque na notificacao
  messaging().onNotificationOpenedApp((remoteMessage) => {
    // Navegar para tela relevante
    console.log("Notificacao aberta:", remoteMessage.data);
  });
}

// Configurar canal Android
async function configurarCanais() {
  await notifee.createChannel({
    id: "default",
    name: "Notificacoes",
    importance: AndroidImportance.HIGH,
  });
}
```

### Deep Linking e Universal Links

```typescript
// React Native - Deep Linking
import { Linking } from "react-native";

// Configurar listener
Linking.addEventListener("url", ({ url }: { url: string }) => {
  handleDeepLink(url);
});

// Verificar URL inicial (app fechado)
Linking.getInitialURL().then((url) => {
  if (url) handleDeepLink(url);
});

function handleDeepLink(url: string): void {
  const parsed = new URL(url);
  if (parsed.hostname === "app.exemplo.com") {
    const path = parsed.pathname;
    if (path.startsWith("/produto/")) {
      const id = path.split("/")[2];
      navigation.navigate("ProdutoDetalhes", { id });
    } else if (path.startsWith("/perfil/")) {
      const id = path.split("/")[2];
      navigation.navigate("PerfilUsuario", { id });
    }
  }
}

// Abrir deep link
Linking.openURL("https://app.exemplo.com/produto/123");
```

### Autenticacao Biometrica

```typescript
import * as LocalAuthentication from "expo-local-authentication";

async function autenticarBiometria(): Promise<boolean> {
  const compativel = await LocalAuthentication.hasHardwareAsync();
  if (!compativel) return false;

  const tipos = await LocalAuthentication.supportedAuthenticationTypesAsync();
  if (tipos.length === 0) return false;

  const resultado = await LocalAuthentication.authenticateAsync({
    promptMessage: "Autenticar para continuar",
    fallbackLabel: "Usar senha",
    cancelLabel: "Cancelar",
  });

  return resultado.success;
}
```

## Testes Mobile

### Testes Unitarios

```typescript
// React Native - Jest
import { renderHook, act } from "@testing-library/react-hooks";
import { useAuthStore } from "./authStore";

describe("useAuthStore", () => {
  it("deve fazer login com sucesso", async () => {
    const { result } = renderHook(() => useAuthStore());

    await act(async () => {
      await result.current.login("ana@email.com", "senha123");
    });

    expect(result.current.autenticado).toBe(true);
    expect(result.current.usuario?.email).toBe("ana@email.com");
  });

  it("deve fazer logout", async () => {
    const { result } = renderHook(() => useAuthStore());

    await act(async () => {
      result.current.logout();
    });

    expect(result.current.autenticado).toBe(false);
    expect(result.current.token).toBeNull();
  });
});
```

```dart
// Flutter - flutter_test
import 'package:flutter_test/flutter_test.dart';
import 'package:meu_app/tela_tarefas.dart';

void main() {
  testWidgets('deve exibir lista de tarefas', (tester) async {
    await tester.pumpWidget(
      MaterialApp(home: TelaTarefas()),
    );

    expect(find.text('Tarefas'), findsOneWidget);
    expect(find.byType(ListView), findsOneWidget);
  });

  testWidgets('deve adicionar nova tarefa', (tester) async {
    await tester.pumpWidget(
      MaterialApp(home: TelaTarefas()),
    );

    await tester.tap(find.byType(FloatingActionButton));
    await tester.pump();

    expect(find.text('Nova tarefa'), findsOneWidget);
  });
}
```

### Testes E2E

```typescript
// Detox - React Native E2E
describe("Fluxo de Autenticacao", () => {
  beforeEach(async () => {
    await device.reloadReactNative();
  });

  it("deve fazer login com sucesso", async () => {
    await element(by.id("emailInput")).typeText("ana@email.com");
    await element(by.id("senhaInput")).typeText("senha123");
    await element(by.id("loginButton")).tap();

    await expect(element(by.id("homeScreen"))).toBeVisible();
    await expect(element(by.text("Bem-vinda, Ana"))).toBeVisible();
  });

  it("deve mostrar erro com credenciais invalidas", async () => {
    await element(by.id("emailInput")).typeText("errado@email.com");
    await element(by.id("senhaInput")).typeText("senhaerrada");
    await element(by.id("loginButton")).tap();

    await expect(element(by.text("Credenciais invalidas"))).toBeVisible();
  });
});
```

## Deploy nas Lojas

### iOS - Certificados e TestFlight

```
Fluxo de Publicacao iOS:
1. Apple Developer Program ($99/ano)
2. Criar App ID no Developer Portal
3. Criar certificado de distribuicao
4. Criar provisioning profile de distribuicao
5. Configurar no Xcode (Signing & Capabilities)
6. Archive (Product -> Archive)
7. Distribuir via App Store Connect
8. TestFlight para testes internos/externos
9. Submeter para review da Apple
```

```yaml
# Fastlane - iOS CI/CD
# fastlane/Fastfile
platform :ios do
  lane :beta do
    increment_build_number
    build_app(scheme: "MeuApp", export_method: "app-store")
    upload_to_testflight(skip_waiting_for_build_processing: true)
  end

  lane :release do
    build_app(scheme: "MeuApp", export_method: "app-store")
    upload_to_app_store(
      submit_for_review: true,
      automatic_release: false,
    )
  end
end
```

### Android - Assinatura e Google Play

```
Fluxo de Publicacao Android:
1. Google Play Console ($25 uma vez)
2. Criar app no console
3. Gerar keystore de assinatura
4. Configurar signing no build.gradle
5. Gerar AAB (Android App Bundle)
6. Upload para Google Play Console
7. Preencher ficha da loja
8. Publicar emInternal Testing -> Beta -> Producao
```

```gradle
// build.gradle - Assinatura
android {
    signingConfigs {
        release {
            storeFile file("meu-app.keystore")
            storePassword System.getenv("KEYSTORE_PASSWORD")
            keyAlias "meu-app"
            keyPassword System.getenv("KEY_PASSWORD")
        }
    }
    buildTypes {
        release {
            signingConfig signingConfigs.release
            minifyEnabled true
            proguardFiles getDefaultProguardFile('proguard-android.txt'), 'proguard-rules.pro'
        }
    }
}
```

### CI/CD para Mobile

```yaml
# GitHub Actions - React Native
name: Mobile CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: npm run lint
      - run: npm run test -- --coverage
      - run: npm run tsc

  build-android:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - uses: actions/setup-java@v4
        with: { java-version: "17" }
      - run: npm ci
      - run: cd android && ./gradlew assembleRelease
      - uses: actions/upload-artifact@v4
        with:
          name: android-release
          path: android/app/build/outputs/apk/release/

  build-ios:
    needs: test
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm ci
      - run: cd ios && pod install
      - run: xcodebuild -workspace MeuApp.xcworkspace -scheme MeuApp -configuration Release
```

## Performance Mobile

### Otimizacao de Bundle

```
React Native:
├── Hermes Engine (compilacao bytecode)
├── Proguard/R8 (minify Android)
├── Tree shaking (remover codigo nao usado)
├── Split APKs por arquitetura (ABI splits)
└── Imagens WebP/AVIF (menor que PNG/JPG)

Flutter:
├── Compilacao AOT (release mode)
├── Tree shaking de widgets
├── --split-debug-info (reduzir tamanho)
├── --split-per-abi (APKs separados)
└── Shrink resources + minify
```

```gradle
// Android - ABI Splits
android {
    splits {
        abi {
            enable true
            reset()
            include "armeabi-v7a", "arm64-v8a", "x86_64"
            universalApk true
        }
    }
}
```

### Otimizacao de Imagens

```typescript
// React Native - Imagens otimizadas
import { Image } from "react-native";
import FastImage from "react-native-fast-image";

// FastImage com cache
<FastImage
  source={{
    uri: "https://cdn.exemplo.com/imagem.webp",
    priority: FastImage.priority.high,
  }}
  cache={FastImage.cacheControl.immutable}
  style={{ width: 200, height: 200 }}
  resizeMode={FastImage.resizeMode.cover}
/>

// Lazy loading com placeholder
<Image
  source={{ uri: imagemUrl }}
  loadingIndicatorSource={require("./placeholder.png")}
  style={{ width: 300, height: 200 }}
/>
```

### Gerenciamento de Memoria

```typescript
// React Native - Evitar memory leaks
import { useEffect, useRef } from "react";
import { AppState } from "react-native";

function useCleanup() {
  const timersRef = useRef<ReturnType<typeof setTimeout>[]>([]);
  const subscriptionsRef = useRef<(() => void)[]>([]);

  useEffect(() => {
    return () => {
      // Limpar todos os timers
      timersRef.current.forEach(clearTimeout);
      // Cancelar todas as subscriptions
      subscriptionsRef.current.forEach(unsub => unsub());
    };
  }, []);

  return {
    addTimer: (fn: () => void, ms: number) => {
      const id = setTimeout(fn, ms);
      timersRef.current.push(id);
      return id;
    },
    addSubscription: (unsub: () => void) => {
      subscriptionsRef.current.push(unsub);
    },
  };
}

// FlatList otimizada
<FlatList
  data={itens}
  keyExtractor={item => item.id}
  renderItem={({ item }) => <ItemMemoizado item={item} />}
  initialNumToRender={10}
  maxToRenderPerBatch={5}
  windowSize={5}
  removeClippedSubviews={true}
  getItemLayout={(data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  })}
/>

// Componente memoizado
const ItemMemoizado = React.memo(({ item }: { item: Item }) => {
  return <View>...</View>;
});
```

### Otimizacao de Startup

```
Cold Start Optimization:
1. Lazy load de modulos nao criticos
2. Evitar trabalho pesado no componentDidMount
3. Usar InteractionManager.runAfterInteractions()
4. Splash screen enquanto carrega
5. Pre-carregar dados essenciais em background
6. Minimizar tamanho do bundle inicial
```

```typescript
// React Native - Startup otimizado
import { InteractionManager } from "react-native";

function App() {
  const [pronto, setPronto] = useState(false);

  useEffect(() => {
    const task = InteractionManager.runAfterInteractions(async () => {
      // Carregar dados essenciais apos interacoes iniciais
      await Promise.all([
        carregarConfiguracao(),
        verificarAtualizacao(),
      ]);
      setPronto(true);
    });

    return () => task.cancel();
  }, []);

  if (!pronto) {
    return <SplashScreen />;
  }

  return <AppPrincipal />;
}
```

## Referencias Cruzadas

- [[frontend]] - Compartilhamento de conceitos com desenvolvimento web
- [[testing-advanced]] - Estrategias avancadas de teste
- [[devops/ci-cd/github-actions]] - CI/CD para aplicacoes mobile
- [[Web-Components]] - Componentes reutilizaveis e padroes de UI
- [[backend]] - Integracao com APIs e servicos backend

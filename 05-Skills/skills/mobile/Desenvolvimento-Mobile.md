---
title: "Desenvolvimento Mobile"
description: "Guia completo de desenvolvimento mobile: React Native, Flutter, iOS nativo (Swift) e Android nativo (Kotlin/Compose). Abrange arquitetura, state management, testes, performance, publicacao e exemplos praticos integrados ao vault."
tags: [mobile, react-native, flutter, swift, kotlin, ios, android, arquitetura-mobile]
nivel: avancado
fonte: ""
updated: 2026-06-07
backlinks: ["05-Skills/skills/ai/INDEX"]
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# Desenvolvimento Mobile

## Visao Geral

Desenvolvimento mobile e a criacao de aplicativos para dispositivos moveis como smartphones e tablets. A escolha entre nativo, hibrido ou cross-platform depende de requisitos de performance, time, custo e complexidade.

### Nativo vs. Hibrido vs. Cross-Platform

| Abordagem | Linguagem | Performance | Acesso nativo | Custo | Exemplos |
|-----------|-----------|-------------|---------------|-------|----------|
| **Nativo Swift** | Swift | Excelente | Total | Alto | App iOS banco |
| **Nativo Kotlin** | Kotlin | Excelente | Total | Alto | App Android banco |
| **Cross-platform RN** | TS/JS | Boa | Bridge/JSI | Medio | Nubank, Shopify |
| **Cross-platform Flutter** | Dart | Excelente | Method Channel | Medio | Google Ads, BMW |
| **Hibrido PWA** | HTML/CSS/JS | Limitada | Restrito | Baixo | Twitter Lite |
| **Hibrido Cordova** | JS | Baixa | Plugins | Baixo | Apps legados |

### Quando usar cada abordagem

**Nativo**: performance maxima, acesso completo a hardware, animacoes complexas (60fps+), AR/VR, jogos, apps bancarios, apps que usam APIs exoticas do SO. Exige duas bases de codigo separadas.

**React Native**: time web que precisa entregar mobile rapido, compartilhamento de logica com web, apps com UI predominantemente de dados (listas, formularios, dashboards). Meta, Shopify, Discord usam RN.

**Flutter**: Google ecosystem, need for pixel-perfect UI, animacoes fluidas sem depender de componentes nativos, startups que querem single codebase com performance nativa. Google Ads, BMW, Toyota usam Flutter.

**Hibrido/PWA**: apps de conteudo, MVP rapidissimo, SEO via PWA, distribuicao sem loja. Nao substitui apps que exigem hardware nativo.

## React Native

### Setup de Projeto

```bash
# Usando React Native CLI (recomendado para apps complexos)
npx react-native@latest init GestorAluguelApp --template react-native-template-typescript

# Usando Expo (recomendado para prototipagem)
npx create-expo-app GestorAluguelApp --template blank-typescript

# Dependencias essenciais
npm install @react-navigation/native @react-navigation/native-stack
npm install @react-navigation/bottom-tabs
npm install react-native-safe-area-context react-native-screens
npm install zustand  # state management leve
npm install react-native-vector-icons
npm install react-hook-form zod @hookform/resolvers  # formularios
npm install react-native-query @tanstack/react-query  # server state
```

### Componentes Fundamentais

```tsx
// GestorAluguelApp/src/components/ImovelCard.tsx
import { View, Text, Image, TouchableOpacity } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

interface ImovelCardProps {
  id: string;
  titulo: string;
  valorAluguel: number;
  endereco: string;
  fotoUrl: string;
  status: 'disponivel' | 'alugado' | 'manutencao';
  onPress: (id: string) => void;
}

export function ImovelCard({
  id, titulo, valorAluguel, endereco, fotoUrl, status, onPress
}: ImovelCardProps) {
  const statusColors = {
    disponivel: '#22c55e',
    alugado: '#3b82f6',
    manutencao: '#f59e0b',
  };

  return (
    <TouchableOpacity
      className="bg-white rounded-xl shadow-sm mb-3 overflow-hidden"
      onPress={() => onPress(id)}
      activeOpacity={0.7}
    >
      <Image
        source={{ uri: fotoUrl }}
        className="w-full h-48"
        resizeMode="cover"
      />
      <View className="p-4">
        <View className="flex-row justify-between items-center">
          <Text className="text-lg font-bold">{titulo}</Text>
          <View
            className="px-2 py-1 rounded-full"
            style={{ backgroundColor: statusColors[status] + '20' }}
          >
            <Text style={{ color: statusColors[status] }} className="text-xs font-semibold">
              {status.charAt(0).toUpperCase() + status.slice(1)}
            </Text>
          </View>
        </View>
        <Text className="text-gray-500 mt-1">{endereco}</Text>
        <View className="flex-row items-center mt-2">
          <Ionicons name="cash-outline" size={16} color="#059669" />
          <Text className="text-green-700 font-bold text-lg ml-1">
            R$ {valorAluguel.toLocaleString('pt-BR')}
          </Text>
          <Text className="text-gray-400 text-sm ml-1">/mes</Text>
        </View>
      </View>
    </TouchableOpacity>
  );
}
```

### Navegacao

```tsx
// GestorAluguelApp/src/navigation/AppNavigator.tsx
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';

type RootStackParamList = {
  MainTabs: undefined;
  ImovelDetalhe: { imovelId: string };
  ContratoForm: { imovelId?: string; contratoId?: string };
  InquilinoDetalhe: { inquilinoId: string };
};

type TabParamList = {
  Dashboard: undefined;
  Imoveis: undefined;
  Inquilinos: undefined;
  Financeiro: undefined;
};

const Stack = createNativeStackNavigator<RootStackParamList>();
const Tab = createBottomTabNavigator<TabParamList>();

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ color, size }) => {
          const icons = {
            Dashboard: 'grid-outline',
            Imoveis: 'home-outline',
            Inquilinos: 'people-outline',
            Financeiro: 'wallet-outline',
          };
          return <Ionicons name={icons[route.name]} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#059669',
        tabBarInactiveTintColor: '#9ca3af',
        headerShown: false,
      })}
    >
      <Tab.Screen name="Dashboard" component={DashboardScreen} />
      <Tab.Screen name="Imoveis" component={ImoveisScreen} />
      <Tab.Screen name="Inquilinos" component={InquilinosScreen} />
      <Tab.Screen name="Financeiro" component={FinanceiroScreen} />
    </Tab.Navigator>
  );
}

export function AppNavigator() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerStyle: { backgroundColor: '#059669' },
          headerTintColor: '#fff',
          headerTitleStyle: { fontWeight: 'bold' },
        }}
      >
        <Stack.Screen
          name="MainTabs"
          component={MainTabs}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="ImovelDetalhe"
          component={ImovelDetalheScreen}
          options={{ title: 'Detalhes do Imovel' }}
        />
        <Stack.Screen
          name="ContratoForm"
          component={ContratoFormScreen}
          options={{ title: 'Contrato' }}
        />
        <Stack.Screen
          name="InquilinoDetalhe"
          component={InquilinoDetalheScreen}
          options={{ title: 'Detalhes do Inquilino' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

### Gerenciamento de Estado

```tsx
// GestorAluguelApp/src/store/imovelStore.ts
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface Imovel {
  id: string;
  titulo: string;
  endereco: string;
  valorAluguel: number;
  status: 'disponivel' | 'alugado' | 'manutencao';
  fotoUrl: string;
  createdAt: Date;
}

interface ImovelStore {
  imoveis: Imovel[];
  selectedId: string | null;
  loading: boolean;
  error: string | null;
  fetchImoveis: () => Promise<void>;
  addImovel: (imovel: Omit<Imovel, 'id' | 'createdAt'>) => Promise<void>;
  updateStatus: (id: string, status: Imovel['status']) => void;
  selectImovel: (id: string | null) => void;
}

export const useImovelStore = create<ImovelStore>()(
  persist(
    (set, get) => ({
      imoveis: [],
      selectedId: null,
      loading: false,
      error: null,

      fetchImoveis: async () => {
        set({ loading: true, error: null });
        try {
          const response = await fetch('https://api.gestor-aluguel.com/imoveis');
          const data = await response.json();
          set({ imoveis: data, loading: false });
        } catch (err) {
          set({ error: 'Falha ao carregar imoveis', loading: false });
        }
      },

      addImovel: async (imovelData) => {
        const newImovel: Imovel = {
          ...imovelData,
          id: Date.now().toString(),
          createdAt: new Date(),
        };
        set((state) => ({ imoveis: [newImovel, ...state.imoveis] }));
      },

      updateStatus: (id, status) => {
        set((state) => ({
          imoveis: state.imoveis.map((i) =>
            i.id === id ? { ...i, status } : i
          ),
        }));
      },

      selectImovel: (id) => set({ selectedId: id }),
    }),
    {
      name: 'imovel-storage',
      storage: createJSONStorage(() => AsyncStorage),
    }
  )
);
```

### Performance

```tsx
// Otimizacao com FlashList (substitui FlatList)
import { FlashList } from '@shopify/flash-list';

function ImoveisList() {
  const { imoveis, selectImovel } = useImovelStore();

  return (
    <FlashList
      data={imoveis}
      renderItem={({ item }) => (
        <ImovelCardMemoized
          {...item}
          onPress={(id) => selectImovel(id)}
        />
      )}
      estimatedItemSize={300}
      keyExtractor={(item) => item.id}
      onEndReachedThreshold={0.5}
      ListEmptyComponent={
        <EmptyState message="Nenhum imovel cadastrado" />
      }
      ItemSeparatorComponent={() => <View className="h-3" />}
    />
  );
}

// Memoizacao de componentes
const ImovelCardMemoized = React.memo(ImovelCard, (prev, next) => {
  return (
    prev.id === next.id &&
    prev.status === next.status &&
    prev.valorAluguel === next.valorAluguel
  );
});
```

**Dicas de performance no React Native**:
- Use `FlashList` em vez de `FlatList` para listas grandes (virtualizacao eficiente)
- Evite re-renders desnecessarios com `React.memo` e `useMemo`
- Use `InteractionManager.runAfterInteractions` para tarefas pesadas pos-navegacao
- Prefira `StyleSheet.create` a estilos inline
- Otimize imagens com `react-native-fast-image`
- Use Hermes como JS engine (habilitado por padrao no RN 0.70+)
- No New Architecture, o JSI permite comunicacao sincrona JS-Native

## Flutter

### Setup de Projeto

```bash
# Criar projeto
flutter create --org com.gestoraluguel --project-name gestor_aluguel --platforms=android,ios gestor_aluguel_app

# Adicionar dependencias (pubspec.yaml)
flutter pub add provider  # state management
flutter pub add go_router  # navegacao declarativa
flutter pub add dio  # HTTP client
flutter pub add flutter_secure_storage
flutter pub add google_fonts
flutter pub add shimmer  # loading skeletons
flutter pub add firebase_core firebase_auth cloud_firestore

# Rodar
flutter run
```

### Widgets Fundamentais

```dart
// lib/screens/imovel_card.dart
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class ImovelCard extends StatelessWidget {
  final String id;
  final String titulo;
  final double valorAluguel;
  final String endereco;
  final String fotoUrl;
  final String status;
  final VoidCallback onTap;

  const ImovelCard({
    super.key,
    required this.id,
    required this.titulo,
    required this.valorAluguel,
    required this.endereco,
    required this.fotoUrl,
    required this.status,
    required this.onTap,
  });

  Color _statusColor() {
    switch (status) {
      case 'disponivel': return Colors.green;
      case 'alugado': return Colors.blue;
      case 'manutencao': return Colors.orange;
      default: return Colors.grey;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      clipBehavior: Clip.antiAlias,
      child: InkWell(
        onTap: onTap,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Image.network(
              fotoUrl,
              height: 200,
              width: double.infinity,
              fit: BoxFit.cover,
              errorBuilder: (context, error, stackTrace) =>
                Container(
                  height: 200,
                  color: Colors.grey[200],
                  child: const Icon(Icons.broken_image, size: 64),
                ),
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Expanded(
                        child: Text(
                          titulo,
                          style: GoogleFonts.inter(
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 4,
                        ),
                        decoration: BoxDecoration(
                          color: _statusColor().withOpacity(0.15),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Text(
                          status[0].toUpperCase() + status.substring(1),
                          style: TextStyle(
                            color: _statusColor(),
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      const Icon(Icons.location_on, size: 16, color: Colors.grey),
                      const SizedBox(width: 4),
                      Text(endereco, style: const TextStyle(color: Colors.grey)),
                    ],
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      const Icon(Icons.attach_money, color: Colors.green),
                      const SizedBox(width: 4),
                      Text(
                        'R\$ ${valorAluguel.toStringAsFixed(2)}',
                        style: GoogleFonts.inter(
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
                          color: Colors.green[700],
                        ),
                      ),
                      const Text('/mes', style: TextStyle(color: Colors.grey)),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

### Navegacao com GoRouter

```dart
// lib/router/app_router.dart
import 'package:go_router/go_router.dart';
import '../screens/dashboard_screen.dart';
import '../screens/imoveis_screen.dart';
import '../screens/imovel_detalhe_screen.dart';
import '../screens/contrato_form_screen.dart';
import '../screens/inquilinos_screen.dart';

final appRouter = GoRouter(
  initialLocation: '/',
  routes: [
    ShellRoute(
      builder: (context, state, child) => MainShell(child: child),
      routes: [
        GoRoute(
          path: '/',
          pageBuilder: (context, state) =>
            MaterialPage(child: DashboardScreen()),
        ),
        GoRoute(
          path: '/imoveis',
          pageBuilder: (context, state) =>
            MaterialPage(child: ImoveisScreen()),
        ),
        GoRoute(
          path: '/inquilinos',
          pageBuilder: (context, state) =>
            MaterialPage(child: InquilinosScreen()),
        ),
      ],
    ),
    GoRoute(
      path: '/imoveis/:id',
      pageBuilder: (context, state) =>
        MaterialPage(
          child: ImovelDetalheScreen(
            imovelId: state.pathParameters['id']!,
          ),
        ),
    ),
    GoRoute(
      path: '/contrato/novo',
      name: 'contratoNovo',
      builder: (context, state) =>
        ContratoFormScreen(),
    ),
    GoRoute(
      path: '/contrato/:id/editar',
      builder: (context, state) =>
        ContratoFormScreen(
          contratoId: state.pathParameters['id'],
        ),
    ),
  ],
);

// Shell com BottomNavigationBar
class MainShell extends StatelessWidget {
  final Widget child;
  const MainShell({super.key, required this.child});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: child,
      bottomNavigationBar: NavigationBar(
        selectedIndex: _calculateIndex(context),
        onDestinationSelected: (index) {
          switch (index) {
            case 0: context.go('/'); break;
            case 1: context.go('/imoveis'); break;
            case 2: context.go('/inquilinos'); break;
          }
        },
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.dashboard_outlined),
            selectedIcon: Icon(Icons.dashboard),
            label: 'Dashboard',
          ),
          NavigationDestination(
            icon: Icon(Icons.home_outlined),
            selectedIcon: Icon(Icons.home),
            label: 'Imoveis',
          ),
          NavigationDestination(
            icon: Icon(Icons.people_outlined),
            selectedIcon: Icon(Icons.people),
            label: 'Inquilinos',
          ),
        ],
      ),
    );
  }

  int _calculateIndex(BuildContext context) {
    final location = GoRouterState.of(context).uri.toString();
    if (location.startsWith('/imoveis')) return 1;
    if (location.startsWith('/inquilinos')) return 2;
    return 0;
  }
}
```

### State Management com Provider

```dart
// lib/providers/imovel_provider.dart
import 'package:flutter/foundation.dart';
import '../models/imovel.dart';
import '../services/imovel_api.dart';

class ImovelProvider extends ChangeNotifier {
  final ImovelApi _api = ImovelApi();

  List<Imovel> _imoveis = [];
  bool _loading = false;
  String? _error;
  String? _selectedId;

  List<Imovel> get imoveis => _imoveis;
  bool get loading => _loading;
  String? get error => _error;
  Imovel? get selected =>
    _imoveis.firstWhereOrNull((i) => i.id == _selectedId);

  Future<void> fetchImoveis() async {
    _loading = true;
    _error = null;
    notifyListeners();

    try {
      _imoveis = await _api.getImoveis();
    } catch (e) {
      _error = 'Falha ao carregar imoveis: $e';
    } finally {
      _loading = false;
      notifyListeners();
    }
  }

  Future<void> addImovel(Imovel imovel) async {
    try {
      await _api.createImovel(imovel);
      _imoveis.insert(0, imovel);
      notifyListeners();
    } catch (e) {
      _error = 'Erro ao adicionar: $e';
      notifyListeners();
    }
  }

  void updateStatus(String id, String novoStatus) {
    final index = _imoveis.indexWhere((i) => i.id == id);
    if (index != -1) {
      _imoveis[index] = _imoveis[index].copyWith(status: novoStatus);
      notifyListeners();
    }
  }

  void selectImovel(String? id) {
    _selectedId = id;
    notifyListeners();
  }
}
```

### Material Design e Tema

```dart
// lib/theme/app_theme.dart
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  static const Color _primary = Color(0xFF059669);
  static const Color _secondary = Color(0xFF065F46);
  static const Color _error = Color(0xFFDC2626);

  static ThemeData light() {
    final colorScheme = ColorScheme.fromSeed(
      seedColor: _primary,
      secondary: _secondary,
      error: _error,
      brightness: Brightness.light,
    );

    return ThemeData(
      useMaterial3: true,
      colorScheme: colorScheme,
      textTheme: GoogleFonts.interTextTheme(),
      cardTheme: CardTheme(
        elevation: 1,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(8),
        ),
        contentPadding: const EdgeInsets.symmetric(
          horizontal: 16,
          vertical: 12,
        ),
      ),
      elevatedButtonTheme: ElevatedButtonThemeData(
        style: ElevatedButton.styleFrom(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
        ),
      ),
      appBarTheme: AppBarTheme(
        centerTitle: true,
        backgroundColor: _primary,
        foregroundColor: Colors.white,
        elevation: 0,
      ),
    );
  }
}
```

## React Native vs. Flutter vs. Nativo (Swift/Kotlin)

### Tabela Comparativa Detalhada

| Criterio | React Native | Flutter | Swift (iOS) | Kotlin (Android) |
|----------|-------------|---------|-------------|-------------------|
| **Linguagem** | TypeScript/JS | Dart | Swift | Kotlin |
| **Curva aprendizado** | Baixa (se sabe React) | Media | Alta | Media-Alta |
| **Performance** | Boa (melhorou com New Arch) | Excelente | Excelente | Excelente |
| **UX Nativa** | Componentes nativos | Canvas proprio | 100% nativa | 100% nativa |
| **Tamanho app** | ~15-30MB | ~20-50MB | ~5-15MB | ~3-10MB |
| **Hot Reload** | Sim | Stateful Hot Reload | Preview | Compose Preview |
| **Compartilhamento codigo** | Web (React Native Web) | Web (Flutter Web) | N/A | N/A |
| **Acesso nativo** | Bridge/JSI | Method Channel | Direto | Direto |
| **Ecossistema libs** | NPM (vasto) | pub.dev (crescendo) | CocoaPods/SPM | Maven/Gradle |
| **Ferramentas dev** | Metro, Flipper, Expo | DevTools, Flutter Inspector | Xcode Instruments | Android Studio |
| **CI/CD** | EAS Build, Fastlane | Codemagic, Fastlane | Xcode Cloud | Firebase Test Lab |
| **Empresas** | Meta, Shopify, Discord, Nubank | Google, BMW, Toyota, nuBank | Apple, Airbnb, Lyft | Google, Uber, Trello |

### Quando usar cada um

**React Native** e ideal quando:
- O time ja tem expertise em React/TypeScript
- Precisa compartilhar codigo com uma aplicacao web existente
- O app e data-driven (listas, formularios, CRUDs)
- Precisa lancar MVP rapidamente com equipe reduzida
- O ecossistema NPM oferece lib que voce precisa

**Flutter** e ideal quando:
- Precisa de UI pixel-perfect identica em ambas plataformas
- Animacoes complexas e transicoes fluidas sao requisitos
- O time pode investir em aprender Dart
- App nao depende de muitas libs nativas exoticas
- Performance e consistencia visual sao prioridades

**Nativo (Swift/Kotlin)** e ideal quando:
- Performance maxima e exigida (jogos, AR, camera em tempo real)
- App usa APIs de hardware de ponta (NFC, Bluetooth LE, HealthKit)
- UX nativa e prioridade (gestos, haptics, Dynamic Island)
- App bancario/financeiro com requisitos rigorosos de seguranca
- Equipe especializada em iOS ou Android

### Estrategia Recomendada

Para o projeto `gestor_aluguel` do vault:
- **Backend**: API REST unica (Node.js ou Laravel)
- **Mobile principal**: React Native com New Architecture (mais rapido de desenvolver, compartilha tipos com web)
- **Alternativa**: Flutter se a UI precisar ser mais rica e performatica
- **Nativo**: Apenas para features especificas (mapas, AR para medir ambientes, escaneamento de documentos)

## Arquitetura Mobile

### MVC (Model-View-Controller)

Padrao classico do iOS (UIKit). ViewController coordena Model e View.

```
/model        -> Dados e regras de negocio
/view         -> Interface (XIB/Storyboard)
/controller   -> Logica de apresentacao
```

**Problema**: Massive View Controller no iOS.

### MVVM (Model-View-ViewModel)

Padrao predominante em Android (Jetpack Compose) e React Native.

```swift
// Swift MVVM
class ImovelViewModel: ObservableObject {
    @Published var imoveis: [Imovel] = []
    @Published var loading = false

    func loadImoveis() {
        loading = true
        api.fetchImoveis { [weak self] result in
            DispatchQueue.main.async {
                self?.imoveis = result
                self?.loading = false
            }
        }
    }
}

struct ImoveisView: View {
    @StateObject var viewModel = ImovelViewModel()

    var body: some View {
        List(viewModel.imoveis) { imovel in
            ImovelRow(imovel: imovel)
        }
        .onAppear { viewModel.loadImoveis() }
    }
}
```

### BLoC (Business Logic Component)

Padrao do Flutter que separa eventos de estados usando Streams.

```dart
// Eventos
abstract class ImovelEvent {}
class CarregarImoveis extends ImovelEvent {}
class AtualizarStatus extends ImovelEvent { final String id; final String status; }

// Estados
abstract class ImovelState {}
class ImovelInitial extends ImovelState {}
class ImovelLoading extends ImovelState {}
class ImovelLoaded extends ImovelState { final List<Imovel> imoveis; }
class ImovelError extends ImovelState { final String message; }

// BLoC
class ImovelBloc extends Bloc<ImovelEvent, ImovelState> {
  final ImovelRepository repository;

  ImovelBloc(this.repository) : super(ImovelInitial()) {
    on<CarregarImoveis>((event, emit) async {
      emit(ImovelLoading());
      try {
        final imoveis = await repository.fetchAll();
        emit(ImovelLoaded(imoveis: imoveis));
      } catch (e) {
        emit(ImovelError(message: e.toString()));
      }
    });
  }
}
```

### Clean Architecture (Robert C. Martin)

Separacao em camadas com dependencias apontando para dentro.

```
src/
  core/           -> Erros, entidades, use cases genericos
  data/           -> Repositorios concretos, DTOs, fontes de dados
    datasources/  -> Remote (API) / Local (DB)
    models/       -> JSON serialization
    repositories/ -> Implementacao dos repositorios
  domain/         -> Regras de negocio (sem dependencia externa)
    entities/     -> Objetos de negocio
    repositories/ -> Contratos abstratos
    usecases/     -> Casos de uso
  presentation/   -> UI, state management, navegacao
    blocs/        -> BLoC / providers
    pages/        -> Telas
    widgets/      -> Componentes reutilizaveis
```

**Para o gestor_aluguel**:

```dart
// domain/entities/imovel.dart
class Imovel {
  final String id;
  final String titulo;
  final double valorAluguel;
  final String endereco;
  final String status;

  const Imovel({
    required this.id,
    required this.titulo,
    required this.valorAluguel,
    required this.endereco,
    required this.status,
  });
}

// domain/repositories/imovel_repository.dart
abstract class ImovelRepository {
  Future<List<Imovel>> fetchAll();
  Future<Imovel> fetchById(String id);
  Future<void> create(Imovel imovel);
  Future<void> updateStatus(String id, String status);
}

// domain/usecases/get_imoveis.dart
class GetImoveis {
  final ImovelRepository repository;
  GetImoveis(this.repository);

  Future<List<Imovel>> call() => repository.fetchAll();
}
```

## APIs e Integracao

### REST API

```typescript
// React Native: API service com Axios
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.gestor-aluguel.com/v1',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
});

api.interceptors.request.use(async (config) => {
  const token = await AsyncStorage.getItem('@auth_token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const imovelService = {
  list: () => api.get<Imovel[]>('/imoveis'),
  getById: (id: string) => api.get<Imovel>(`/imoveis/${id}`),
  create: (data: Omit<Imovel, 'id'>) => api.post<Imovel>('/imoveis', data),
  update: (id: string, data: Partial<Imovel>) => api.patch(`/imoveis/${id}`, data),
  delete: (id: string) => api.delete(`/imoveis/${id}`),
};
```

### GraphQL

```graphql
# Query
query ListarImoveis {
  imoveis {
    id
    titulo
    valorAluguel
    endereco
    status
    inquilino { nome contato }
  }
}

mutation CriarImovel($input: ImovelInput!) {
  criarImovel(input: $input) { id titulo }
}

subscription StatusAtualizado {
  imovelAtualizado { id status }
}
```

```dart
// Flutter: GraphQL com ferry
class ImovelGraphQLService {
  Future<List<Imovel>> getImoveis() async {
    const query = r'''
      query ListarImoveis {
        imoveis { id titulo valorAluguel endereco status }
      }
    ''';
    final response = await client.request(GqlRequest(query: query));
    return (response.data['imoveis'] as List)
      .map((json) => Imovel.fromJson(json))
      .toList();
  }
}
```

### Firebase

```typescript
// React Native: Firebase Auth + Firestore
import auth from '@react-native-firebase/auth';
import firestore from '@react-native-firebase/firestore';

export async function login(email: string, password: string) {
  return auth().signInWithEmailAndPassword(email, password);
}

export function subscribeImoveis(callback: (imoveis: Imovel[]) => void) {
  return firestore()
    .collection('imoveis')
    .where('proprietarioId', '==', auth().currentUser?.uid)
    .onSnapshot((snapshot) => {
      const imoveis = snapshot.docs.map((doc) => ({
        id: doc.id,
        ...doc.data(),
      })) as Imovel[];
      callback(imoveis);
    });
}
```

### Push Notifications

```typescript
// React Native: Firebase Cloud Messaging
import messaging from '@react-native-firebase/messaging';

export async function setupNotifications() {
  const granted = await messaging().requestPermission();
  if (granted === messaging.AuthorizationStatus.AUTHORIZED) {
    const token = await messaging().getToken();
    await api.post('/devices', { token, platform: 'mobile' });
  }
}

messaging().onMessage(async (remoteMessage) => {
  // Notificacao em foreground
  notifee.displayNotification({
    title: remoteMessage.notification?.title,
    body: remoteMessage.notification?.body,
    android: { channelId: 'alugueis', pressAction: { id: 'default' } },
  });
});

messaging().setBackgroundMessageHandler(async (remoteMessage) => {
  // Tratamento em background
  if (remoteMessage.data?.type === 'pagamento_recebido') {
    await updateLocalData(remoteMessage.data);
  }
});
```

## Publicacao

### App Store (iOS)

```bash
# 1. Configurar certificados e profiles
fastlane match development --read-only

# 2. Build de producao
cd ios && xcodebuild -workspace GestorAluguel.xcworkspace \
  -scheme GestorAluguel \
  -configuration Release \
  -sdk iphoneos \
  -archivePath ./build/GestorAluguel.xcarchive \
  archive

# 3. Upload para App Store Connect
xcodebuild -exportArchive \
  -archivePath ./build/GestorAluguel.xcarchive \
  -exportOptionsPlist exportOptions.plist \
  -exportPath ./build/ipa

xcrun altool --upload-app -f ./build/ipa/GestorAluguel.ipa \
  -u $APPLE_ID -p $APP_SPECIFIC_PASSWORD
```

**Requisitos**:
- Certificado de desenvolvedor Apple ($99/ano)
- App Store Connect record
- Screenshots em todos os tamanhos de tela
- Politica de privacidade
- Revisao humana (24-72h)

### Google Play (Android)

```bash
# 1. Gerar keystore
keytool -genkey -v -keystore release.keystore \
  -alias gestor_aluguel -keyalg RSA -keysize 2048 -validity 10000

# 2. Build AAB
cd android && ./gradlew bundleRelease

# 3. Sign bundle
jarsigner -keystore release.keystore \
  app/build/outputs/bundle/release/app-release.aab \
  gestor_aluguel

# 4. Upload via Google Play Console ou fastlane
fastlane supply --aab app/build/outputs/bundle/release/app-release.aab \
  --skip_upload_screenshots --skip_upload_metadata
```

**Requisitos**:
- Conta Google Play Developer ($25 unico)
- AAB (Android App Bundle)
- Screenshots
- Teste interno/aberto obrigatorio para contas novas

### CI/CD Mobile

```yaml
# .github/workflows/mobile-ci.yml
name: Mobile CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  lint-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 20 }
      - run: npm ci
      - run: npx eslint .
      - run: npx jest --coverage

  build-android:
    needs: lint-and-test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: echo "ANDROID_KEYSTORE_BASE64=${{ secrets.ANDROID_KEYSTORE }}" >> $GITHUB_ENV
      - run: npm ci
      - run: npx react-native build-android --mode release

  build-ios:
    needs: lint-and-test
    runs-on: macos-14
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npx react-native build-ios --mode release

  deploy-eas:
    needs: [build-android, build-ios]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npx eas-cli build --platform all --profile production --non-interactive
        env:
          EXPO_TOKEN: ${{ secrets.EXPO_TOKEN }}
```

### Automacao com Fastlane

```ruby
# fastlane/Fastfile
default_platform(:android)

platform :android do
  desc "Build e deploy Android para Google Play"
  lane :deploy do
    gradle(task: 'clean')
    gradle(task: 'bundleRelease')
    upload_to_play_store(
      track: 'production',
      aab: 'app/build/outputs/bundle/release/app-release.aab',
      release_status: 'completed',
      metadata_path: 'fastlane/metadata/android'
    )
  end
end

platform :ios do
  desc "Build e deploy iOS para App Store"
  lane :deploy do
    match(type: 'appstore', readonly: true)
    build_app(
      workspace: 'ios/GestorAluguel.xcworkspace',
      scheme: 'GestorAluguel',
      configuration: 'Release',
      export_method: 'app-store'
    )
    upload_to_app_store(skip_metadata: true, skip_screenshots: true)
  end
end
```

## Exemplos Praticos: Gestor de Aluguel

### Arquitetura Recomendada para o Projeto

```
gestor_aluguel_app/
  src/
    core/
      api/              -> Axios config, interceptors
      storage/          -> AsyncStorage abstraction
      theme/            -> Tema global
      utils/            -> Formatadores, validadores
    modules/
      auth/             -> Login, registro, recovery
      dashboard/        -> Resumo financeiro, graficos
      imoveis/          -> CRUD de imoveis, fotos
      inquilinos/       -> CRUD de inquilinos, historico
      contratos/        -> Geracao de contratos, assinatura
      financeiro/       -> Pagamentos, boletos, relatorios
      manutencao/       -> Solicitacoes, ordens de servico
    shared/
      components/       -> ImovelCard, StatusBadge, Button
      hooks/            -> useAuth, usePagination, useDebounce
      types/            -> Typescript types globais
    navigation/         -> Stack + Tab navigators
```

### Funcionalidades Chave

**Dashboard**: graficos de receita mensal, ocupacao, inadimplencia, proximos vencimentos. Usar `react-native-chart-kit` ou `victory-native`.

**Imoveis**: cadastro com fotos (react-native-image-picker), localizacao com mapa (react-native-maps), status tracking.

**Inquilinos**: cadastro com CPF/CNPJ validacao, score de credito via API, historico de pagamentos.

**Contratos**: template HTML convertido para PDF (react-native-html-to-pdf), assinatura digital (react-native-signature-canvas), envio por email.

**Financeiro**: integracao com ASAAS ou Mercado Pago para geracao de boletos, registro de pagamentos via PIX, extrato mensal.

### Checklist de Implementacao

- [ ] Definir arquitetura (Clean Architecture + MVVM recomendado)
- [ ] Configurar projeto com TypeScript
- [ ] Implementar autenticacao (email/senha + biometria)
- [ ] Setup de navegacao (Stack + BottomTabs)
- [ ] Tela de dashboard com indicadores
- [ ] CRUD de imoveis com upload de fotos
- [ ] CRUD de inquilinos
- [ ] Geracao de contratos em PDF
- [ ] Integracao financeira (boletos, PIX)
- [ ] Push notifications (lembretes de pagamento)
- [ ] Modo offline (AsyncStorage + sync)
- [ ] Testes unitarios e de integracao
- [ ] CI/CD com EAS Build ou Fastlane
- [ ] Publicacao nas lojas

## Referencias e Links

- [[05-Skills/skills/02-software-engineering/mobile-development]] - Nota complementar de desenvolvimento mobile
- [[04-Conhecimentos/07-Humanidades/Programacao/Arquitetura-de-Software]] - Fundamentos de arquitetura
- [[05-Skills/skills/ai/INDEX]] - Indice de habilidades de IA
- React Native Docs: https://reactnative.dev
- Flutter Docs: https://flutter.dev
- SwiftUI Tutorials: https://developer.apple.com/tutorials/swiftui
- Kotlin Multiplatform: https://kotlinlang.org/docs/multiplatform.html
- Fastlane: https://fastlane.tools
- Expo: https://expo.dev
